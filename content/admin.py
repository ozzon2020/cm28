from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from adminsortable2.admin import SortableAdminMixin
from content.models import Razdel, Chast,Section,Block
from common.fields import OrderField
from pytils.translit import slugify
import textwrap
from django.utils.html import strip_tags
import re
from django import forms
from django.forms import Textarea, TextInput 
from content.forms import SectionForm,RazdelForm
from django.templatetags.static import static
from rutermextract import TermExtractor
# Register your models here.

from razdel import sentenize
from common.utils import make_desc_title
#from django.contrib import admin

#admin.site.index_template = 'memcache_status/admin_index.html'

make_desc_title.short_description = "Генерация - title, meta_description, meta_keywords"     
    
    
class ChastInline(admin.StackedInline):
    model = Chast
    exclude = ('id','var_id','sort')
    extra = 0       
    
@register(Razdel)
class RazdelAdmin(SortableAdminMixin,SummernoteModelAdmin,ModelAdmin):
    #readonly_fields = ('namefile',)
    
    list_display = ('name', 'id','namefile','active','block_active')

    summernote_fields = [('name','block' ), ('sort', 'active')]
    summernote_fields = '__all__'
    list_editable=['active']
    #inlines = [RazdelAdminInline]
    #actions = [make_active]
    fieldsets = (
         ('Технические параметры', {
             'fields': (('name', 'namefile'),('title', 'image','image2'),  
         ( 'meta_description','meta_keywords'),)
             }),
         ('Содержание', {
             'classes': (),
             'fields': ('main','about',('block', 'block_active'), 'active'),
             
             }),
     )  
    list_per_page = 15
    list_filter = ('created',)
    #save_on_top=True
    #actions = [make_desc_title]
    form=RazdelForm
    inlines = [ChastInline]
    #inlines = [RazdelAdminInline]
    icon_name = 'storage'

    class Meta:
        verbose_name_plural = "Раздел"  


class SectionInline(admin.StackedInline):
        model = Section
        exclude = ('main','created','stattext',)
        extra = 0          
        
#admin.site.register(Razdel, RazdelAdmin)        
@register(Chast)
class ChastAdmin(SortableAdminMixin,SummernoteModelAdmin,ModelAdmin):
        #readonly_fields = ('namefile',)
        
        list_display = ('name', 'id','var_id','active',)
    
        #summernote_fields = [('name','block' ), ('sort', 'active')]
        #summernote_fields = '__all__'
        list_editable=['active']
        #inlines = [RazdelAdminInline]
        #actions = [make_active]
        inlines = [SectionInline]
        list_per_page = 15
        list_filter = ('var_id',)
        #save_on_top=True
        
        
        #inlines = [RazdelAdminInline]
        icon_name = 'crop_square'
    
        class Meta:
            verbose_name_plural = "Части"  

          
class PageRelationInline(admin.StackedInline):
        model = Section
        exclude = ('name','created','stattext',)
        extra = 0              
        
@register(Section)
class SectionAdmin(SortableAdminMixin,SummernoteModelAdmin,ModelAdmin):
        
        fieldsets = (
                 ('Технические параметры', {
                     'fields': (('name', 'namefile','created'),('title', 'image'),  
        ( 'meta_description','meta_keywords'),)
                     }),
                 ('Содержание', {
                     'classes': (),
                     'fields': ('main',('ch', 'active','productlink'),('sloganheader','top_page'),('tags'),('stattext'),'pages'),
                     }),
             )     
        list_display = ('sort','name','pk', 'namefile','tag_list','sort', 'created','active')
        list_display_links = ( "name" , )
        list_filter = ('ch','ch__var','created','namefile')
        list_editable=['created','active']
            #list_editable=['total_view',]
        search_fields = ('@name', 'namefile','@main')
            #list_editable=('namefile',)
            #summernote_fields = '__all__'
        summernote_fields = ('main','sloganheader','top_page')
            #actions_on_top = False
            #save_on_top=True
            #actions_on_bottom = True
            #active.admin_order_field = 'sort'
        #inlines = [PageRelationInline]
        form=SectionForm
        list_per_page = 15
        actions = [make_desc_title]
        icon_name = 'pages'
        def get_queryset(self, request):
            return super().get_queryset(request).prefetch_related('tags')
        
        def tag_list(self, obj):
            return ", ".join(o.name for o in obj.tags.all())
        tag_list.short_description = "Тэги"
        
        class Meta:
            verbose_name_plural = "Страницы"   
            ordering = ['-sort']         
            
@register(Block)
class BlockAdmin(SortableAdminMixin,SummernoteModelAdmin,ModelAdmin):
    #readonly_fields = ('namefile',)
    
    list_display = ('name', 'id','slug','created','active',)
    
    summernote_fields = [('name','block' ), ('sort', 'active')]
    summernote_fields = '__all__'
    list_editable=['active']
    #inlines = [RazdelAdminInline]
    #actions = [make_active]
    fieldsets = (
         ('Технические параметры', {
             'fields': (('name', 'slug',),('title', 'image'), 
                        ( 'meta_description','meta_keywords'),
         )
             }),
         ('Содержание', {
             'classes': (),
             'fields': (('main', 'active')),
             
             }),
     )  
    list_per_page = 15
    list_filter = ('created',)
    #save_on_top=True
    
    
    #inlines = [RazdelAdminInline]
    icon_name = 'dehaze'
    
    class Meta:
        verbose_name_plural = "Блоки"              