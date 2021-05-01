from django.contrib.sitemaps import Sitemap
from content.models import Razdel, Section
from qs.models import Qs
#from blog.models import Post,PostComment
from shop.models import Category,Product
from django.utils import timezone
from django.urls import reverse
from django.utils.timezone import now
from taggit.models import Tag
#from taggit.managers import TaggableManager

class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.4
    protocol ='https'


    def items(self):
        return Tag.objects.all()
 
    def location(self,obj):
        #return section_list_by_tag'/blog/%s' % (obj.article_slug)  
        return '/tag/%s/' % (obj.slug)

    
class QsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6
    protocol ='https'

    def items(self):
        return Qs.objects.filter(created__lte=timezone.now()).filter(active__exact=True).all().order_by('-created')
        #return ['qs:qs-detail', 'qs:qs-detail']
  
    
    def lastmod(self, obj):
        return obj.created  

    #def location(self, item):
        #return reverse(item)      

    

class HomeSitemap(Sitemap):
    priority = 0.5         # Приоритет
    changefreq = 'daily'   # Частота проверки
    protocol ='https'
 
    # Метод, возвращающий массив с url-ками
    def items(self):
        return ['content:index', 'content:index']
 
    # Метод непосредственной экстракции url из шаблона
    def location(self, item):
        return reverse(item)      

class ContentSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol ='https'

    def items(self):
        return Section.objects.filter(created__lte=timezone.now()).filter(active__exact=True).all().order_by('-sort')
        #return Section.objects.filter(active__exact=True).exclude(var__namefile__in=['news','about']).all().order_by('-sort')

    def lastmod(self, obj):
        return obj.updated


    
class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7
    protocol ='https'

    def items(self):
        return Category.objects.filter(active__exact=True).all().order_by('-sort')
        #return Section.objects.filter(active__exact=True).exclude(var__namefile__in=['news','about']).all().order_by('-sort')

    #def lastmod(self, obj):
        #return obj.updated
    def lastmod(self, obj):
        time=now()
        return time    
    
class ShopSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6
    protocol ='https'

    def items(self):
        return Product.objects.filter(active__exact=True).filter(created__lte=timezone.now()).all().order_by('-created')

    def lastmod(self, obj):
        return obj.created    