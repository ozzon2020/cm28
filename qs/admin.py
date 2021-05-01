from django.db import models
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from adminsortable2.admin import SortableAdminMixin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.
from qs.models import  ThemeQs,Qs
#from content.models import  Razdel
from common.fields import OrderField
from django import forms
#from taggit.models import Tag, TaggedItem
#from material.admin.decorators import register
#from material.admin.options import MaterialModelAdmin
#from material.admin.sites import site
from datetime import datetime
#from django.utils.text import slugify
#from pytils.translit import slugify

#from taggit.managers import TaggableManager
from django.conf import settings
#from django.contrib.auth.models import User
#from account.models import  Profile
from django.utils.safestring import mark_safe
from django.http import HttpResponse

# Register your models here.

class QsInline(admin.StackedInline):
        model = Qs
        exclude = ('updated','created',)
        extra = 0          
        
#admin.site.register(Razdel, RazdelAdmin)        
@register(ThemeQs)
class ThemeQsAdmin(SortableAdminMixin,SummernoteModelAdmin,ModelAdmin):
        #readonly_fields = ('namefile',)
        
        list_display = ('name', 'id','active',)
    
        #summernote_fields = [('name','block' ), ('sort', 'active')]
        #summernote_fields = '__all__'
        list_editable=['active']
        #inlines = [RazdelAdminInline]
        #actions = [make_active]
        inlines = [QsInline]
        list_per_page = 15
        #list_filter = ('var',)
        #save_on_top=True
        
        
        #inlines = [RazdelAdminInline]
        icon_name = 'assignment'
    
        class Meta:
                verbose_name_plural = "Темы" 


@register(Qs)
class QsAdmin(SummernoteModelAdmin,ModelAdmin):


        
        list_display = ['pk','name','theme','active','replyoff','created',]
        list_display_links = ('pk','name','theme' )
        #list_select_related = ('user','direction' )
        list_filter = [('created', DateRangeFilter),'id','replyoff','var']
        list_editable=['created','active',]
        list_per_page = 20
        #readonly_fields=('headshot_image',)
        #list_select_related = ('user', )
        #autocomplete_fields = ['user',]
        #search_fields = ['user__first_name']
        #actions = [export_to_txt]
        summernote_fields = ('reply',)
    
        
        #def first_name(self, obj):
                #return obj.user.first_name
        #first_name.short_description = 'First Name'
        #def last_name(self, obj):
                #return obj.user.last_name
          
        #def get_name(self):
                #return '{} {}'.format(self.first_name, self.last_name)
        
        #User.add_to_class("__str__", get_name)
         
        #def get_user(self, obj):
                #return obj.user.get_full_name
        #get_user.short_description = "User"
        #user=self.user
        fieldsets = (
                   ('Технические параметры', {
                       'fields': (('var','theme'), ('name',),)
                       }),
                   ('Содержание', {
                       'classes': (),
                       'fields': (('main'),('reply'),('active','replyoff','created'),),
                       }),
                  
               )            
    
    
        icon_name = 'question_answer'
        #filter_horizontal=('users_like',)
        

        
        
        class Meta:
                verbose_name_plural = "Вопросы-Ответы" 
                ordering = ['-created'] 
                #exclude = ['user']

#admin.site.register(Qs, QsAdmin)                