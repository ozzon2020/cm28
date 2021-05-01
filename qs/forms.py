from django import forms
from django.core.mail import send_mail
from django.conf import settings
from qs.models import ThemeQs,Qs
#from content.models import Razdel
#from django.contrib.auth.models import User, Group
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
#from common.utils import  SummernoteWidgetWithCustomToolbar
#from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
#from django_summernote.fields import SummernoteTextField
#from django.contrib.auth.models import User
     
#from haystack.forms import SearchForm
from django import forms




        
class QsForm(forms.ModelForm):
    
    captcha = ReCaptchaField(label="")
    def __init__(self, *args, **kwargs):
        super(QsForm, self).__init__(*args, **kwargs)
                                    #required=True)    
    class Meta:
        model = Qs          
        fields = ('var','theme','name','email','main',) 
     
        #widgets = {'main': SummernoteWidgetWithCustomToolbar()}
        
    def send_email(self):
        subject = 'Новый вопрос от {} '.format(self.cleaned_data['name'])
        message = 'Тема: {}\nВопрос:\n{} '.format(self.cleaned_data['theme'],self.cleaned_data['name'],
                                                            self.cleaned_data['email'],self.cleaned_data['main'],)
        send_mail(subject, message, settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER])     
        #send_mail(subject, message, 'admin@myblog.com',['admin@myblog.com'])       
        
#class SayingForm(forms.ModelForm):
    ##captcha = ReCaptchaField(required=False,label="")
    #class Meta:
        #model = Saying
        #widgets = {'body': SummernoteWidgetWithCustomToolbar(),}
        #fields = ('body',)   
        
        
class ReplyForm(forms.ModelForm):
    #captcha = ReCaptchaField(required=False,label="")
    class Meta:
        model = Qs
        fields = ('reply',)        