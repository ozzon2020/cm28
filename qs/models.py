from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
#from django.forms import ModelForm
#from django.utils.text import slugify
#from pytils.translit import slugify
from common.fields import OrderField
#from taggit.managers import TaggableManager
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import now
from datetime import datetime
#from django.utils.timezone
#from django.utils.timezone import now
#from taggit.models import Tag, TaggedItem

class ThemeQs(models.Model):
        
        name = models.CharField(max_length=200, verbose_name="Темы вопросов",help_text="Подраздел")
        sort = OrderField(blank=True, verbose_name="<>", help_text="Порядок сортировки")
        active = models.BooleanField(default=True,verbose_name="Статус")
        #active = models.CharField(max_length=2, choices=ACTIVE_STATUS, blank=True, verbose_name="Статус", default='on', help_text='Статус - Вкл/Выкл')   
    
        class Meta:
                verbose_name_plural = "Темы вопросов"  
                ordering = ["-sort"]    
    
        def __str__(self):
    
                return self.name 


class Qs(models.Model):  
        name = models.CharField(max_length=250,verbose_name="Имя", help_text="Имя")
        theme = models.CharField(max_length=250, verbose_name="Тема вопроса", help_text="О чем вопрос ")
        email = models.CharField(max_length=250,verbose_name="E-mail",)
        main = models.TextField(max_length=40000,verbose_name="Вопрос", help_text="Заданный вопрос")
        reply = models.TextField(max_length=40000, null=True,blank=True,verbose_name="Ответ", help_text="Ответ")
        var = models.ForeignKey('ThemeQs', verbose_name="Тема", on_delete=models.SET_NULL, null=True,related_name='qstheme')
        created = models.DateTimeField(default=datetime.now,editable=True,verbose_name="Создание",help_text="Дата Создания")
        updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
        
        sort = OrderField(blank=True, verbose_name="Порядок сортировки",help_text="Порядок сортировки")
        replyoff=models.BooleanField(default=False,blank=True,verbose_name="Ответ") 
        active = models.BooleanField(default=True,verbose_name="Статус")
        
        
        class Meta:
                verbose_name_plural = "Вопрос - Ответ" 
                #db_table = 'questions_qs'
                ordering = ['-created']    
        
        def save(self, *args, **kwargs):
                if  self.reply !='':
                        self.replyoff = True
                        #create_action(self.user, 'Ответ врача','reply',self.user)
                        if not self.id:
                                self.created = now() 
                super(Qs, self).save(*args, **kwargs)    
        
        def get_absolute_url(self):
                return reverse('qs:qs-detail', kwargs={'pk': self.pk})   
                 
                        #return reverse('question:qs-detail', kwargs={'razdel_slug':self.var.namefile,'pk': self.pk})    
        
        
        
        def __str__(self):
                
                return "Тема {} ".format(self.theme) 