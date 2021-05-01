from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords,truncatewords_html,safe,striptags
from django.utils import timezone
from .models import Section
from yaturbo import YandexTurboFeed



class YTurboFeed(YandexTurboFeed):
    
    title = "Материалы 28cm.ru "
    link = "/turbo_content/"     
    #turbo_sanitize = True
    def item_title(self, item):
        return item.title
    
    def items(self):
        return Section.objects.all().filter(active=True).filter(created__lte=timezone.now()).order_by('-ch')

    def item_turbo(self, item):
        # Представим, что в атрибуте article.html содержится код страницы.
        # Ввиду того, что мы проставили выше turbo_sanitize = True
        # наш HTML будет санирован - теги и атрибуты, не поддерживаемые 
        # Турбо-страницами, будут автоматически удалены.
        # Это, конечно не то же самое, что сверстать специальную Турбо-страницу,
        # но в ряде случаев и этого достаточно.
        return truncatewords(item.main,100)   
    
