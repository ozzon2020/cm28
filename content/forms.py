from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .models import Razdel,Section

from material.admin import widgets
from django.contrib.auth.models import User
#from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from common.utils import  SummernoteWidgetWithCustomToolbar

 
#class ContactForm(forms.Form):
    #name = forms.CharField(max_length=25,label="Имя")
    #email = forms.EmailField(label="Почта")
    #comments = forms.CharField(required=True,widget=forms.Textarea,label="Сообщение")
    #captcha = ReCaptchaField(label="")
    
    #def send_email(self):
        ## send email using the self.cleaned_data dictionary
        ##subject = '{} ({}) сообщение с сайта  '.format(valid_data['name'], valid_data['email'])
        ##message = 'Имя автора: {}\n\n\' сообщение: {}'.format(valid_data['name'], valid_data['comments'])
        ##send_mail(subject, message, valid_data        ['email'],[valid_data['name']])  
        ##The subject, message, from_email and recipient_list parameters are required.      
        ##send_mail('Сообщение от'+self.cleaned_data['name'], self.cleaned_data['comments'],self.cleaned_data['email'], [settings.EMAIL_HOST_USER])        
        #send_mail('Сообщение от '+self.cleaned_data['name']+' '+self.cleaned_data['email'], self.cleaned_data['comments'],settings.EMAIL_HOST_USER, 
#[settings.EMAIL_HOST_USER])
        ##send_mail('Сообщение от '+self.cleaned_data['name']+' '+self.cleaned_data['email'], self.cleaned_data['comments'], 'admin@myblog.com',['admin@myblog.com'],)        
   
      

#class CommentForm(forms.ModelForm):
    
    ##captcha = ReCaptchaField(label="")
    ##captcha = ReCaptchaField(label="")
    
    #def __init__(self, *args, **kwargs):
        #self.user = kwargs.pop('user')  # To get request.user. Do not use kwargs.pop('user', None) due to potential security hole

        #super(CommentForm, self).__init__(*args, **kwargs)
        
    #class Meta:
        #model = Comment
        ##widgets = {'body': SummernoteWidgetWithCustomToolbar()}
        #widgets = {'body': SummernoteWidgetWithCustomToolbar(),} 
        #fields = ('body',)
        
    
        
    #def send_email(self):
        #subject = 'Новый комментарий {} '.format(self.user.first_name)
        #message = 'Комментарий : \n{} от {} '.format(self.cleaned_data['body'],self.user.username)
        ##send_mail(subject, message, settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER])     
        #send_mail(subject, message, 'admin@myblog.com',['admin@myblog.com'])     
    ## forms.py
class SectionForm(forms.ModelForm):
    title = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    meta_description = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    meta_keywords = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    #top_page = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    #sloganheader = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))

    class Meta:
        model = Section    
        fields = ('__all__')  
        
#class ArticleForm(forms.ModelForm):
    #title = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    #meta_description = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    #meta_keywords = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    ##stattext = forms.CharField( widget=forms.Textarea(attrs={'rows': 15, 'cols': 100}))
    #class Meta:
        #model = Article
        #fields = ('__all__')  
        
class RazdelForm(forms.ModelForm):
    title = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    meta_description = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    meta_keywords = forms.CharField( widget=forms.Textarea(attrs={'style': 'height:80px;font-size:1.1em;'}))
    class Meta:
        model = Razdel
        fields = ('__all__')   