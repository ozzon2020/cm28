from django_summernote.admin import SummernoteModelAdmin
from django.contrib.admin import ModelAdmin, register
from django.contrib import admin
from shop.models import Category, Product, MedRazdel, Order, OrderItem,Review
from content.models import Section
from adminsortable2.admin import SortableAdminMixin
import csv
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from .forms import ProductForm,MedRazdelForm,CategoryForm
from django.utils import timezone
from django.db.models import Sum
from common.utils import make_product_title,make_category_product
from decimal import *
#from material.admin.decorators import register
#from material.admin.options import MaterialModelAdmin
#from material.admin.sites import site

make_product_title.short_description = "Генерация - title, meta_description, meta_keywords"  

def order_detail(obj):
    return mark_safe('<a href="{}">Детали</a>'.format(
        reverse('shop:admin_order_detail', args=[obj.id])))

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;''filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
 
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Экспорт в CSV'


def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('shop:admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'Invoice'

class CategoryInline(admin.StackedInline):
        model = Category
        exclude = ('name','active','slug',)
        extra = 0  
        
class SectionInline(admin.StackedInline):
        model = Section
        exclude = ('title','meta_description','meta_keywords','image','main','stattext','created','update','sort','tags',)
        extra = 0  
        ordering=['name']

@register(MedRazdel)
class MedRazdelAdmin(SortableAdminMixin,SummernoteModelAdmin,ModelAdmin):
    list_display = ['id','sort','name','namefile','active']
    list_display_links = ( "name" , 'namefile',)
    prepopulated_fields = {'namefile': ('name',)}
    list_editable = ['active']
    icon_name = 'view_module'
    list_per_page = 15
    inlines = [CategoryInline]
    summernote_fields = ('about',)
    fieldsets = (
    ('Технические параметры', {
    'fields': (('name', 'namefile','image',),('active', 'created'),  
    )}),
    ('Содержание', {
             'classes': (),
             'fields': ('about',),
             }),
     )   
    class Meta:
        verbose_name_plural = "Разделы препаратов"   
        ordering = ['-name']

@register(Category)
class CategoryAdmin(SortableAdminMixin,SummernoteModelAdmin,ModelAdmin):
    list_display = ['name','var','slug','active']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['active']
    list_filter = ['var',]
    form=CategoryForm 
    icon_name = 'view_week'
    list_per_page = 15
    actions = [make_category_product]
    summernote_fields = ('description',)
    fieldsets = (
    ('Технические параметры', {
    'fields': (('name', 'var','slug',),'title',('meta_description','meta_keywords'),('active', ),  
    )}),
    ('Содержание', {
             'classes': (),
             'fields': ('description','stattext'),
             }),
     )      
    class Meta:
        verbose_name_plural = "Категории"   
        ordering = ['-sort']
        
@register(Product)
class ProductAdmin(SortableAdminMixin,SummernoteModelAdmin,ModelAdmin):
    list_display = ['name', 'final_rating','total_raiting','slug', 'price','category','available','active', ]
    list_filter = ['name', 'created','category','category__var__name',]
    list_editable = ['price', 'active','available']
    prepopulated_fields = {'slug': ('name',)}
    form=ProductForm   
    actions = [make_product_title]
    inlines = [SectionInline]
    icon_name = 'store'
    actions = [make_product_title]
    summernote_fields = ('description','sostav','about')
    #filter_horizontal=('users_like','users_dislike',)

    
    def final_rating(self, obj):
        #return obj.id
        #for obj in queryset:
        count_raiting=Review.objects.filter(active__exact=True).filter(product__exact=obj.id).filter(created__lte=timezone.now()).count()
        summa_raiting=Review.objects.filter(active__exact=True).filter(product__exact=obj.id).filter(created__lte=timezone.now()).all().aggregate(Sum('rating'))
        if(count_raiting==0 or summa_raiting==0):
            fin_raiting=0
        else:
            fin_raiting=float(summa_raiting['rating__sum']) / float(count_raiting)
    #spk = kwargs['section_pk']
    #return Comment.active.count()
        return round(fin_raiting, 2)
    final_rating.short_description = "Оценка" 

    
    
    list_per_page = 20
    fieldsets = (
    ('Технические параметры', {
    'fields': (('name', 'slug', 'price',),'title',('meta_description','meta_keywords'),'image',('active','available', ),  
    )}),
    ('Содержание', {
             'classes': (),
             'fields': (('about','sostav'), ('priem','kurs','sertifikat'),'izgotovitel','description',('category','best', 'sale','orderlink'),
                        ('created','total_raiting'),('stattext')),
             }),
     )   
    def save_model(self, request, obj, form, change):
        
        count_raiting=Review.objects.filter(active__exact=True).filter(product__exact=obj.id).filter(created__lte=timezone.now()).count()
        summa_raiting=Review.objects.filter(active__exact=True).filter(product__exact=obj.id).filter(created__lte=timezone.now()).all().aggregate(Sum('rating'))
        if(count_raiting==0 or summa_raiting==0):
            fin_raiting=0
        else:
            fin_raiting=Decimal(summa_raiting['rating__sum']) / Decimal(count_raiting)  
            
        obj.total_raiting = fin_raiting
        super().save_model(request, obj, form, change)
        
    class Meta:
        verbose_name_plural = "Препарат"   
        ordering = ['-sort']    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    icon_name = 'add_shopping_cart'

@register(Review)
class ReviewAdmin(SummernoteModelAdmin,ModelAdmin):
    #form = CommentAdminForm
    list_display = ['product','id','name','rating','created','active']
    #readonly_fields=('get_name','headshot_image',)
    summernote_fields = ('body',)
    #list_filter = [('created', DateRangeFilter),'section__var__name','section__name',]
    list_filter = ['product__category__name','product','email']
    list_editable=['rating','created','active']
    list_per_page = 20
    
    fieldsets = (
         ('Пользователь', {
             'fields': (('name','email','product',),('rating','active','created',))
             }),
         ('Параметры', {
             'fields': (('body',))
             }),
     )      
    search_fields = ('product__name',)
    
    
    icon_name = 'face'
    #save_on_top=True
    #def headshot_image(self, obj):
        #if obj.user.profile.photo:
            #return mark_safe('<img src="/media/{url}" width="{width}" height={height} />'.format(
                #url = obj.user.profile.photo,
                #width=32,
                #height=32,))
    #headshot_image.short_description = "Юпик"    
    
    #def get_name(self, obj):
        #return obj.user.first_name +' '+ obj.user.last_name  
    #get_name.short_description = "Имя"
    
    class Meta:
        verbose_name_plural = "Отзывы" 


@register(Order)
class OrderAdmin(ModelAdmin):
    actions = [export_to_csv]
    list_display = ['id', 'first_name','last_name', 'summa', 
                    'postal_code','city', 'address', 'paid',
                    'created', 'payment', 
                    order_detail,
                    order_pdf]
    list_filter = ['paid', 'created', 'payment']
    inlines = [OrderItemInline]  
    icon_name = 'shopping_basket'
