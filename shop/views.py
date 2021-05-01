from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Category, Product,OrderItem,Order,Review,MedRazdel
from content.models import Section
from .cart import Cart
from django.views.generic.edit import CreateView
from shop.forms import CartAddProductForm,OrderCreateForm,PostReview,FormWithCaptcha
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
import json
from decimal import Decimal
from django.http import JsonResponse
#from hitcount.views import HitCountDetailView

from common.decorators import ajax_required
from django.core.mail import EmailMessage
from io import BytesIO
from common.menumixin import MenuMixin
from django.views import generic
from django.views.generic.edit import FormView,FormMixin
from django.urls import  reverse,reverse_lazy
from django.utils import timezone
from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView
from actions.utils import create_action
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
#from common.utils import image_html_clean
from common.decorators import ajax_required
from smtplib import SMTPException
import errno
from socket import error as socket_error
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from decimal import *
from django.db.models import Sum

class MedRazdelDetailView(generic.ListView):
    model = MedRazdel
    #slug_field='namefile'
    #category = None
    template_name = 'shop/razdel-list.html'
    #count_hit = True
    #category = ''

    #def get_queryset(self, **kwargs):
        ##return self.model.objects.filter(active__exact=True).all() 
        #if self.kwargs:
            #self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
            ##self.category=self.kwargs['category_slug']
            #return self.model.objects.filter(active__exact=True).filter(slug__exact=self.category.slug).all() 
        #else:    
            #return self.model.objects.filter(active__exact=True).all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_item']=True

        #context['image_top'] ='hf030.jpg'
        #context['image_bot'] ='hf031.jpg'
        #context['razdel'] = self.razdel
        #context['orders_item']=True

        return context
 

class CategoryDetailView(generic.DetailView):
    model = Category
    #slug_field='namefile'
    #category = None
    template_name = 'shop/category-list.html'
    #count_hit = True
    #category = ''
    #def get_queryset(self):
        #return self.model.objects.filter(active__exact=True).all() 
    def get_queryset(self, **kwargs):
        #return self.model.objects.filter(active__exact=True).all() 
        if self.kwargs:
            self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
            #self.category=self.kwargs['category_slug']
            return self.model.objects.filter(active__exact=True).filter(slug__exact=self.category.slug).all() 
        else:    
            return self.model.objects.filter(active__exact=True).all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object).filter(active__exact=True).filter(created__lte=timezone.now()).all()
        context['shop_item']=True
        #context['image_top'] ='hf030.jpg'
        #context['image_bot'] ='hf031.jpg'
        #context['razdel'] = self.razdel
        #context['orders_item']=True
        context['sloganheader']=  '<h1> '+self.object.var.name +' - '+self.object.name+'</h1><p>'+self.object.title+'</p>'
        return context



    
class ProductDetailView(FormMixin,generic.DetailView):
    model=Product
    #date_field='publish'
    #month_format='%m'
    paginate_by = 5
    template_name = 'shop/product/product_detail.html'
    form_class = PostReview
    cart_product_form = CartAddProductForm()
    #count_hit = True
    
    def review(self,request):
        review=Review.objects.filter(product=self.object).filter(active__exact=True).filter(created__lte=timezone.now())
        object_list = review
        review_all=object_list.count()
        paginator = Paginator(object_list, self.paginate_by) # по 3 поста на каждой странице
        page = request.GET.get('page')
        try:
            review = paginator.page(page)
        except PageNotAnInteger:
                # Если страница не является целым числом,   авляем первую страницу
            review = paginator.page(1)
        except EmptyPage:
            if request.is_ajax():
                # If the request is AJAX and the page is out of range
                # return an empty page
                return HttpResponse('')            
            # Если страница вне диапазо  н а  отправляем последнюю страницу результатов
            review = paginator.page(paginator.num_pages) 
           
        return  review  
    def get_form_kwargs(self):
        kwargs = super(ProductDetailView, self).get_form_kwargs()
        return kwargs  
    
    def get_success_url(self):

        return reverse_lazy('shop:product_detail', kwargs={'slug':self.category.slug,'slug':self.object.slug})  

    def post(self, request, *args, **kwargs):
            
        #if not self.request.user.is_authenticated:
            #return HttpResponseRedirect("/account/login/")

        
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            
            #captcha_score = form.cleaned_data['captcha'].get('score')
            get_recaptcha = request.POST.get("g-recaptcha-response")
            return self.form_valid(form)
        else:
            success_message = '<div class="header">Ваш отзыв не добавлен</div> <p>Вы не правильно заполнили форму.Проверьте пожалуйста...</p>'
            messages.error(self.request, success_message)
            return self.form_invalid(form)
        
           
            #return self.form_invalid(form)
            #print(form)
            #print("Invalid Form")
            #print(form.errors)              
            #return HttpResponseRedirect("/qs/")
            #return HttpResponseRedirect(self.object.get_absolute_url())
        
    
        
    def form_valid(self, form):

        Review.objects.create(
            product=self.object,
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            body=form.cleaned_data['body'],
            rating=form.cleaned_data['rating'],
            active=True
        )
        count_raiting=Review.objects.filter(active__exact=True).filter(product__exact=self.object.id).filter(created__lte=timezone.now()).count()
        summa_raiting=Review.objects.filter(active__exact=True).filter(product__exact=self.object.id).filter(created__lte=timezone.now()).all().aggregate(Sum('rating'))
 
        p = Product.objects.get(id=self.object.id)    
        p.total_raiting=Decimal(summa_raiting['rating__sum']) / Decimal(count_raiting)
        p.save()
  
        create_action(form.cleaned_data['name'], 'Отзыв о продукте','bullhorn', self.object)
        
        success_message = '<div class="header">Ваш отзыв о продукте опубликован </div> <p>Спасибо за Вашу активность.</p>'
        messages.success(self.request, success_message)
        #return super().form_valid(form) 
        return HttpResponseRedirect(self.object.get_absolute_url())
          
    
    def get_queryset(self):

        return self.model.objects.filter(active__exact=True).filter(created__lte=timezone.now()).all()        
    
    
    def get_context_data(self, *args, **kwargs):
        #object_list =Review.objects.filter(product=self.object).filter(active__exact=True).filter(created__lte=timezone.now())
        
        context = super().get_context_data(**kwargs)
        context['comments'] = self.review(self.request)
        context['form'] = self.get_form()
        context['cart_product_form']=CartAddProductForm()
        context['page'] =self.request.GET.get('page')
        context['sectionsprod'] = Section.objects.filter(productlink=self.object).filter(active__exact=True).filter(created__lte=timezone.now()).all()
        #context['recaptcha_site_key']=settings.RECAPTCHA_PUBLIC_KEY
        context['captcha'] = FormWithCaptcha,
        context['shop_item']=True
        context['sloganheader']=  '<h1> '+self.object.category.name+' - '+self.object.name+'</h1><p>'+self.object.title+'</p>'
        #context['direction_menu'] = Direction.objects.filter(active__exact=True).all()
        #context['date_field']=int(self.date_field.year)
        return context      




@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('shop:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    if cart:
        return redirect('shop:cart_detail')
    #return redirect('shop/product/1/novital.html')
    return redirect('shop:razdel-list')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'],
                                       'update': True})    
    return render(request, 'shop/cart/detail.html', 
                        {'cart': cart,
                        'step':1,
                        'orders_item': True
                         })

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            create_action(order.first_name+' '+order.last_name, 'На сумму '+str(order.summa)+' руб.','bullhorn', order)
            #request.session['order_a'] = form
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # create invoice e-mail
            subject = 'Интернет магазин preparation.su - Инвойс № {}'.format(order.id)
            message = 'Пожалуйста, прочтите прилагаемый счет-фактуру за вашу недавнюю покупку'
            email = EmailMessage(subject,message,settings.EMAIL_HOST_USER,[order.email])
            #email = EmailMessage(subject,message,order.email,[settings.EMAIL_HOST_USER,])
            # generate PDF
            html = render_to_string('shop/cart/order_pdf.html', {'order': order})
            out = BytesIO()
            stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
            weasyprint.HTML(string=html).write_pdf(out,stylesheets=stylesheets)
            # attach PDF file
            email.attach('order_{}.pdf'.format(order.id),out.getvalue(),'application/pdf')
            # send e-mail
            try:
                email.send()
                
            #send admin
            except socket_error as serr:
                if serr.errno != errno.ECONNREFUSED:
                    # Not the error we are looking for, re-raise
                    raise serr            
            except SMTPException as e:
                error_code,error_msg = e.smtp_code, e.smtp_error
                print(error_msg)
            subject = 'Заказ № {}'.format(order.id)
            message = 'Поступил {},\n\nзаказ на сайте preparation.su .Заказ от {}. на сумму {} email {}'.format(order.first_name,order.id,order.summa,order.email)
            #email = EmailMessage(subject,message,'admin@myshop.com',[order.email])            
            email = EmailMessage(subject,message,settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER])            
            try:
                email.send()
            #send admin
            except socket_error as serr:
                if serr.errno != errno.ECONNREFUSED:
                    # Not the error we are looking for, re-raise
                    raise serr
                
            except SMTPException as e:
                error_code,error_msg = e.smtp_code, e.smtp_error
                print(error_msg)
            
            # очистить корзину
            cart.clear()
            return render(request,
                          'shop/cart/end_order.html',
                          {'order': order,'form': form,'step':3,'sect': 'order',})
    else:
        form = OrderCreateForm()
    return render(request,
                  'shop/cart/order_created.html',
                  {'cart': cart,
                   'form': form,
                   'step':2,
                   'orders_item': True,
                  })



@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                      'shop/cart/order_detail.html',
                      {'order': order})    

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('shop/cart/order_pdf.html',{'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response,
        stylesheets=[weasyprint.CSS(
            settings.STATIC_ROOT + 'css/pdf.css')])
    return response



#@login_required
@csrf_exempt
@require_POST
@ajax_required
def payment(request):
    cart = Cart(request)
    pay_id = request.POST.get('id')

    total_price=str(request.POST.get('pr'))[:-3]
    if pay_id:
        if int(pay_id) ==1:
            #sum(Decimal)
            pay=Decimal(350)
            summa=Decimal(int(pay)+int(total_price))
            return JsonResponse({'status':'ok','name':'Оплата наличными','pay':pay,'summa':summa})
        elif int(pay_id) ==2:
            pay=int(int(total_price)*0.17)
            summa=Decimal(int(pay)+int(total_price))
            return JsonResponse({'status':'ok','name':'Наложенный платеж +17%','pay':pay,'summa':summa})
        else:
            pay=Decimal(500)
            summa=Decimal(int(pay)+int(total_price))
            return JsonResponse({'status':'ok','name':'Через Сбербанк','pay':pay,'summa':summa})

    return JsonResponse({'status':'ko'})

