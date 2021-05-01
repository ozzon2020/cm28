#from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Action
#from material.admin.decorators import register
#from material.admin.options import MaterialModelAdmin
#from material.admin.sites import site
#from account.models import Profile
from django.utils.safestring import mark_safe

@register(Action)
class ActionAdmin(ModelAdmin):
    list_per_page = 20
    list_display = ('name', 'target', 'verb', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)
    icon_name = 'rv_hookup'
    #readonly_fields=('get_name','headshot_image')
    
    #def get_name(self, obj):
        #return obj.user.first_name +' '+ obj.user.last_name  
    #get_name.short_description = "Имя"
    
    #def headshot_image(self, obj):
        #if obj.user.profile.photo:
            #return mark_safe('<img src="/media/{url}" width="{width}" height={height} />'.format(
                #url = obj.user.profile.photo,
                #width=32,
                #height=32,))
    #headshot_image.short_description = "Юпик"       
# Register your models here.
    #target.short_description = 'Название'
    class Meta:
        verbose_name_plural = "Действия"  

