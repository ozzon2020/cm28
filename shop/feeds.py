from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords,truncatewords_html,safe,striptags
from django.utils import timezone
from shop.models import Category,Product
from yaturbo import YandexTurboFeed
 

class YTurboCategory(YandexTurboFeed):
    
    title = "Категории препаратов 28cm.ru "
    link = "/items/"     
    #turbo_sanitize = True
    def item_title(self, item):
        return item.title
    
    def items(self):
        return Category.objects.all().filter(active=True).order_by('-sort')

    def item_turbo(self, item):
        # Представим, что в атрибуте article.html содержится код страницы.
        # Ввиду того, что мы проставили выше turbo_sanitize = True
        # наш HTML будет санирован - теги и атрибуты, не поддерживаемые 
        # Турбо-страницами, будут автоматически удалены.
        # Это, конечно не то же самое, что сверстать специальную Турбо-страницу,
        # но в ряде случаев и этого достаточно.
        return truncatewords(item.description,70)   
    

class YTurboProduct(YandexTurboFeed):
    
    title = "Пролукты на 28cm.ru "
    link = "/items/product/"     
    #turbo_sanitize = True
    def item_title(self, item):
        return item.title
    
    def items(self):
        return Product.objects.all().filter(active=True).filter(created__lte=timezone.now()).order_by('-category')

    def item_turbo(self, item):
        # Представим, что в атрибуте article.html содержится код страницы.
        # Ввиду того, что мы проставили выше turbo_sanitize = True
        # наш HTML будет санирован - теги и атрибуты, не поддерживаемые 
        # Турбо-страницами, будут автоматически удалены.
        # Это, конечно не то же самое, что сверстать специальную Турбо-страницу,
        # но в ряде случаев и этого достаточно.
        return truncatewords(item.description,90)   