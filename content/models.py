from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.forms import ModelForm
from django.utils.text import slugify
from pytils.translit import slugify
from common.fields import OrderField
from taggit.managers import TaggableManager
from django.conf import settings
from django.utils import timezone
from shop.models import Product
#from django.utils.timezone
from django.utils.timezone import now
from taggit.models import Tag, TaggedItem

class RuTag(Tag):
    class Meta:
        proxy = True

    def slugify(self, tag, i=None):
        return slugify(self.name)[:128]

class RuTaggedItem(TaggedItem):
    class Meta:
        proxy = True

    @classmethod
    def tag_model(cls):
        return RuTag

class MenuManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(var__namefile='page').filter(active='1').order_by('sort')



class Razdel(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название раздела",help_text="Название раздела")
    namefile = models.SlugField(max_length=100,null=True, blank=True,verbose_name="Путь к категории", help_text="Путь к категории") 
    title = models.CharField(max_length=250, verbose_name="Титл страницы", help_text="Титл раздела")
    meta_description = models.CharField(max_length=250,verbose_name="Мета раздела",)
    meta_keywords = models.CharField(max_length=250,verbose_name="КейВорд раздела", )    
    image = models.ImageField(verbose_name="Первое",null=True,blank=True,upload_to='razdel/%Y/%m/%d/')
    image2 = models.ImageField(verbose_name="Второе изображение",null=True,blank=True,upload_to='razdel/%Y/%m/%d/')
    about = models.TextField(max_length=40000,verbose_name="", help_text="О разделе")
    main = models.TextField(max_length=40000,verbose_name="",)  
    stattext = models.TextField(max_length=40000,verbose_name="Статистика текста", help_text="Статистика текста")
    sort = OrderField(blank=True, verbose_name="<>", help_text="Порядок сортировки")
    #var = models.ForeignKey('Direction', verbose_name="Направление", on_delete=models.SET_NULL, null=True,related_name='directionrazdel')
    block = models.TextField(max_length=40000,null=True,blank=True,verbose_name="Баннер", help_text="Баннер")
    block_active = models.BooleanField(default=True,verbose_name="Баннер")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата ")
    #ACTIVE_STATUS = (
        #('on', 'Включенно '),
            #('of', 'Выключенно'),
    #)
    active = models.BooleanField(default=True,verbose_name="Статус")
    #active = models.CharField(max_length=2, choices=ACTIVE_STATUS, blank=True, verbose_name="Статус", default='on', help_text='Статус - Вкл/Выкл')   



    def save(self, *args, **kwargs):
        if not self.namefile:self.namefile = slugify(self.name)
        super(Razdel, self).save(*args, **kwargs)      

    class Meta:
        verbose_name_plural = "Раздел"  
        ordering = ["-sort"]    

    #def get_absolute_url(self):

        #return reverse('content:razdel-detail', kwargs={'slug': self.namefile})  

    def __str__(self):

        return self.name 
    
 
class Chast(models.Model):
        name = models.CharField(max_length=200, verbose_name="Часть раздела",help_text="Подраздел")
        var = models.ForeignKey('Razdel', verbose_name="Раздел", on_delete=models.SET_NULL, null=True,related_name='chastrazdel')
        sort = OrderField(blank=True, for_fields=['razdel'],verbose_name="<>", help_text="Порядок сортировки")
        active = models.BooleanField(default=True,verbose_name="Статус")
        #active = models.CharField(max_length=2, choices=ACTIVE_STATUS, blank=True, verbose_name="Статус", default='on', help_text='Статус - Вкл/Выкл')   
    
    
        class Meta:
            verbose_name_plural = "Часть"  
            ordering = ["-sort"]    
    
        def __str__(self):
    
            return self.name   
        '''
        CREATE TABLE `mh_page` (
          `id` smallint(5) NOT NULL DEFAULT '0',
          `name` varchar(150) DEFAULT NULL,
          `navigator` varchar(200) NOT NULL,
          `title_site` varchar(250) DEFAULT NULL,
          `meta_description` varchar(250) NOT NULL,
          `meta_keywords` varchar(250) NOT NULL,
          `sloganheader` text NOT NULL,
          `left_page` text NOT NULL,
          `pages` varchar(200) NOT NULL,
          `top_page` text NOT NULL,
          `main_page` text,
          `podrazdel` int(11) DEFAULT NULL,
          `sort` smallint(5) DEFAULT NULL,
          `active` varchar(5) DEFAULT NULL
        ) ENGINE=MyISAM DEFAULT CHARSET=utf8;
        '''
class Section(models.Model):
        
        name = models.CharField(max_length=250,verbose_name="Название", help_text="Название страницы")
        namefile = models.SlugField(max_length=100,verbose_name="Имя файла", blank=True, help_text="Имя файла")
        title = models.CharField(max_length=250, verbose_name="Титл страницы", help_text="Титл страницы")
        meta_description = models.CharField(max_length=250,verbose_name="Мета страницы",)
        meta_keywords = models.CharField(max_length=250,verbose_name="КейВорд страницы", )
        #sloganheader = models.CharField(max_length=250,verbose_name="Слоган страницы",null=True, blank=True, help_text="Слоган страницы")  
        image = models.ImageField(verbose_name="Изображение",null=True,blank=True,upload_to='pub/%Y/%m/')
        top_page = models.TextField(max_length=500,verbose_name="Вверх страницы",)
        sloganheader = models.TextField(max_length=1000,verbose_name="Слоган страницы", )
        main = models.TextField(max_length=60000,verbose_name="Содержание",)
        stattext = models.TextField(max_length=40000,verbose_name="Статистика текста", help_text="Статистика текста")
        #pages = models.CharField(max_length=250,verbose_name="Ещё страницы",null=True, blank=True,)
        #var = models.ForeignKey('Razdel', verbose_name="Раздел", on_delete=models.SET_NULL, null=True,related_name='sectionrazdel')
        ch = models.ForeignKey('Chast', verbose_name="Подраздел", on_delete=models.SET_NULL, null=True,related_name='chrazdel')
        #leftreklama = models.CharField(max_length=250,null=True, blank=True,)
        created = models.DateTimeField(default=now,editable=True,verbose_name="Создание",help_text="Дата Создания")
        updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
        productlink = models.ForeignKey(Product,verbose_name="Продукт",
                                     on_delete=models.SET_NULL, blank=True,null=True,related_name='pageproduct',help_text="Продукт")
        pages = models.ManyToManyField('self', symmetrical = False,  null = True, blank = True, verbose_name="Ещё страницы")
        #countword = models.CharField(max_length=250,null=True, blank=True,)
        #total_view = models.PositiveIntegerField(db_index=True,default=0,verbose_name="Просмотры")
        #hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation',verbose_name="Просмотры")
        sort = OrderField(blank=True, verbose_name="<>",help_text="Порядок сортировки")
        #ACTIVE_STATUS = (
            #('on', 'Включенно '),
                #('of', 'Выключенно'),
        #)
        #active = models.CharField(max_length=2, choices=ACTIVE_STATUS, blank=True, verbose_name="Статус",default='on', help_text='Статус - Вкл/Выкл')  
        active = models.BooleanField(default=True,verbose_name="Статус")
        tags = TaggableManager(blank=True,through='RuTaggedItem')
        objects = models.Manager() # The default manager.
        menu_objects = MenuManager()
    
        class Meta:
            verbose_name_plural = "Страницы" 
    
            ordering = ["-sort"]    
    
        def get_absolute_url(self):
    
            return reverse('content:section-detail', kwargs={'slug': self.namefile})    
    
        def save(self, *args, **kwargs):
            if not self.namefile:
                self.namefile = slugify(self.name)
            if not self.id:
                self.created = now()        
            super(Section, self).save(*args, **kwargs)    
    
        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name       
class Block(models.Model,):
            
        name = models.CharField(max_length=250,verbose_name="Название", help_text="Название страницы")
        slug = models.SlugField(max_length=100,verbose_name="Имя файла", blank=True, help_text="Имя файла")
        title = models.CharField(max_length=250, verbose_name="Титл страницы", help_text="Титл страницы")
        meta_description = models.CharField(max_length=250,verbose_name="Мета страницы",)
        meta_keywords = models.CharField(max_length=250,verbose_name="КейВорд страницы", )            
        image = models.ImageField(verbose_name="Первое",null=True,blank=True,upload_to='block/%Y/')
        main = models.TextField(max_length=40000,verbose_name="Содержание",)
       
        created = models.DateTimeField(default=now,editable=True,verbose_name="Создание",help_text="Дата Создания")
        enddate = models.DateTimeField(default=now,editable=True,verbose_name="Окончание",help_text="Дата окончания")
        updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
        sort = OrderField(blank=True, verbose_name="<>",help_text="Порядок сортировки")
        
        active = models.BooleanField(default=True,verbose_name="Статус")
    
        class Meta:
            verbose_name_plural = "Блоки" 
    
            ordering = ["-sort"]    
    
        #def get_absolute_url(self):
    
            #return reverse('content:section-detail', kwargs={'slug_dir':self.var.var.slug,'slug_razdel':self.var.namefile,'slug': self.namefile})    
    
        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug= slugify(self.name)
            if not self.id:
                self.created = now()        
            super(Block, self).save(*args, **kwargs)    
    
        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name         