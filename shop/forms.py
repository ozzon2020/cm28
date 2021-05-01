from django import forms
from .models import Order,Category,Review,MedRazdel
#from common.utils import  SummernoteWidgetWithCustomToolbar
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int,label="Количество")
    #quantity = forms.TypedChoiceField(label='Количество',coerce=int, widget=forms.Select(choices=PRODUCT_QUANTITY_CHOICES))
    update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput,label="")
    
class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(label="")

class PostReview(forms.ModelForm):
    #captcha = ReCaptchaField(label="")
    #captcha = ReCaptchaField(label="")
    RAITING_STATUS = (
        ('0', 'Отрицательно'),
        ('1', 'Не очень'),
        ('2', 'Средне'),
        ('3', 'Нормально'),
        ('4', 'Хорошо'),
        ('5', 'Отлично'),
    )
    rating= forms.CharField(label='Как вы оцените препарат ?', widget=forms.RadioSelect(choices=RAITING_STATUS))
    body = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:120px;'}),label="Ваше мнение")

    
    def __init__(self, *args, **kwargs):
        super(PostReview, self).__init__(*args, **kwargs)
                                    #required=True)    
    class Meta:
        model = Review          
        fields = ('rating','name','email','body') 
        
        
        
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment','first_name', 'last_name', 'email', 'postal_code','city', 'address',
                   'phone','summa']    
        widgets = {'summa': forms.HiddenInput()}
        #,'summa'
class ProductForm(forms.ModelForm):
    title = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}),label="Заголовок")
    meta_description = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}),label="Мета Description")
    meta_keywords = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}),label="Ключевые слова")
    priem = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:120px;font-size:1.1em;'}), label="Как принимать")
    #sostav = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:120px;font-size:1.1em;'}), label="Состав")
    kurs = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}), label="Курс приема")
    total_raiting = forms.DecimalField(max_digits=5,decimal_places=2,label="Общий рейтинг")
    
class CategoryForm(forms.ModelForm):
    title = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}),label="Заголовок")
    meta_description = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}),label="Мета Description")
    meta_keywords = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}),label="Ключевые слова")
        
class MedRazdelForm(forms.ModelForm):
    #title = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    name = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    #meta_keywords = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))

    class Meta:
        model = MedRazdel    
        fields = ['name','about', 'active', 'created', 'namefile']            
        #fields = ('__all__')      