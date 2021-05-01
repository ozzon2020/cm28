from django.db import models
from django.urls import reverse
from common.fields import OrderField
#from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
#from content.models import Section
from django.utils.timezone import now
#from haystack import indexes

class MedRazdel(models.Model):
    
    name = models.CharField(max_length=200,db_index=False, verbose_name="Название раздела",help_text="Название раздела")
    namefile = models.SlugField(max_length=100,null=True, blank=True,verbose_name="Путь к категории", help_text="Путь к категории") 
    image = models.ImageField(upload_to='medrazdel/%Y/%m',
                              blank=True, verbose_name="Изображение")
    about = models.TextField(max_length=40000,verbose_name="", help_text="О разделе")

    created = models.DateTimeField(default=now,editable=True, verbose_name="Дата ")
    sort = OrderField(blank=True,verbose_name="<>", help_text="Порядок сортировки")
    #ACTIVE_STATUS = (
        #('on', 'Включенно '),
            #('of', 'Выключенно'),
    #)
    active = models.BooleanField(default=True,verbose_name="Статус")
    #active = models.CharField(max_length=2, choices=ACTIVE_STATUS, blank=True, verbose_name="Статус", default='on', help_text='Статус - Вкл/Выкл')   



    def save(self, *args, **kwargs):
        if not self.namefile:self.namefile = slugify(self.name)
        super(MedRazdel, self).save(*args, **kwargs)      

    class Meta:
        verbose_name_plural = "Раздел"  
        ordering = ["-sort"]    

    def get_absolute_url(self):

        return reverse('shop:razdel-list', kwargs={'slug': self.namefile})  

    def __str__(self):

        return self.name 

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True, verbose_name="Название")
    title = models.CharField(max_length=250, verbose_name="Титл категории", help_text="")
    meta_description = models.CharField(max_length=250,verbose_name="Мета категории",)
    meta_keywords = models.CharField(max_length=250,blank=True,verbose_name="КейВорд категории", )  
    var = models.ForeignKey('MedRazdel', verbose_name="Раздел", on_delete=models.SET_NULL, null=True,related_name='medrazdel')
    description = models.TextField(blank=True, verbose_name="Описание")
    sort = OrderField(blank=True,verbose_name="Порядок сортировки", help_text="Порядок сортировки")
    slug = models.SlugField(max_length=200,verbose_name="Слаг",
                            unique=True)
    active = models.BooleanField(default=True,verbose_name="Статус")
    stattext = models.TextField(max_length=40000,verbose_name="Статистика текста", help_text="Статистика текста")
    
    class Meta:
        ordering = ('-sort',)
        verbose_name = 'category'
        verbose_name_plural = 'Категории'
        
    def get_absolute_url(self):
        return reverse('shop:category-list',args=[self.slug])        

    def __str__(self):
        return self.name

class Product(models.Model,):
    category = models.ForeignKey(Category,verbose_name="Категория",
                                 on_delete=models.SET_NULL,null=True,related_name='products',)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    title = models.CharField(max_length=250, verbose_name="Титл страницы", help_text="Титл препарата")
    meta_description = models.CharField(max_length=250,verbose_name="Мета препарата",)
    meta_keywords = models.CharField(max_length=250,blank=True,verbose_name="КейВорд препарата", )
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="Слаг")
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True, verbose_name="Изображение")
    about = models.TextField(blank=True, verbose_name="Краткое пояснение",help_text="Краткое пояснение")
    description = models.TextField(blank=True, verbose_name="Описание")
    priem = models.TextField(blank=True, max_length=1000,verbose_name="Как принимать",help_text="Как принимать")
    sostav = models.TextField(blank=True, verbose_name="Состав",help_text="Состав")
    kurs = models.CharField(max_length=550,blank=True, verbose_name="Курс приема",help_text="Курс приема")
    izgotovitel = models.CharField(max_length=550,blank=True, verbose_name="Производитель",help_text="Производитель")
    sertifikat = models.CharField(max_length=250,blank=True, verbose_name="Сертификат",help_text="Сертификат")
    #pagelink = models.ForeignKey(Section,verbose_name="Страницы продукта",
                                 #on_delete=models.SET_NULL, null=True,related_name='pageproduct',help_text="Порядок сортировки")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True,verbose_name="Стоимость")
    available = models.BooleanField(default=True, verbose_name="В наличии")
    sort = OrderField(blank=True,verbose_name="Порядок сортировки", help_text="Порядок сортировки")
    created = models.DateTimeField(default=now,editable=True, verbose_name="Когда создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновление")
    
    best = models.CharField(blank=True,max_length=200, db_index=True, verbose_name="Лучший товар")
    sale = models.CharField(blank=True,max_length=200, db_index=True, verbose_name="Скидка")
    orderlink = models.CharField(blank=True,max_length=200, db_index=True, verbose_name="Где купить")
    stattext = models.TextField(max_length=40000,verbose_name="Статистика текста", help_text="Статистика текста")

    
    total_raiting = models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Оценка")
    active = models.BooleanField(default=True,verbose_name="Статус")

    class Meta:
        verbose_name_plural = "Товары"  
        ordering = ('-sort',)
        index_together = (('id', 'slug'),)
        
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.category.slug, self.slug])        

    def __str__(self):
        return self.name

class Review(models.Model): 
    
    
    product = models.ForeignKey(Product,
                                 on_delete=models.CASCADE,
                                 related_name='reviews',limit_choices_to={'active': True},verbose_name="Продукт")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Имя")   
    email = models.EmailField(max_length = 150,verbose_name="E-mail")
    body = models.TextField(verbose_name="Отзыв",) 
    
    created = models.DateTimeField(default=now,editable=True,verbose_name="Создание",)
    modified = models.DateTimeField(default=now,editable=True,verbose_name="Обновление",)    
    active = models.BooleanField(default=True,verbose_name="Статус",help_text="Вкл / Выкл") 
    #total_likes = models.PositiveIntegerField(db_index=True,default=0,verbose_name="Общее количество лайков")
    RAITING_STATUS = (
        ('0', 'Плохо'),
        ('1', 'Не очень'),
        ('2', 'Средне'),
        ('3', 'Нормально'),
        ('4', 'Хорошо'),
        ('5', 'Отлично'),
    )

    rating = models.CharField(
        max_length=1,
        choices=RAITING_STATUS,
        blank=True,
        default='0',
        help_text='Оценка',
        verbose_name="Оценка"
    )
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = now()
        self.modified = now()
        return super(Review, self).save(*args, **kwargs)
    
    class Meta: 
        ordering = ('-created',) 
        verbose_name_plural = "Отзывы"
        
    #def __str__(self): 
        #return 'Отзыв {} о продукте {}'.format(self.user.first_name, self.product.name)         
    
    def get_absolute_url(self):
        
        return reverse('shop:product_detail', args=[self.id,])
    
class Order(models.Model):
    
    PAY_STATUS = (
         ('1', 'Оплата наличными'),
         ('2', 'Наложенный платеж'),
         ('3', 'Через Сбербанк'),
         )
    
    first_name = models.CharField(max_length=150, verbose_name="Фамилия")
    last_name = models.CharField(max_length=50, verbose_name="Имя, Отчество")
    email = models.EmailField(verbose_name="E-mail")
    city = models.CharField(max_length=100, verbose_name="Город")
    postal_code = models.CharField(max_length=20, verbose_name="Индекс")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    payment = models.CharField(max_length=2, choices=PAY_STATUS, verbose_name="Метод оплаты", help_text='Метод оплаты')    
    summa = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма заказа")   
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновление")
    paid = models.BooleanField(default=False, verbose_name="Оплачен")
    

    class Meta:
        verbose_name_plural = "Заказы"  
        ordering = ('-created',)

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE, verbose_name="Продукт")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity    
