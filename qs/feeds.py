from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords,truncatewords_html,safe,striptags
from django.utils import timezone
from .models import Qs
from yaturbo import YandexTurboFeed
#from markdown import markdown

class YQuestionsFeed(YandexTurboFeed):
    title = "Вопросы ответы на 28.ru"
    link = '/feeds/'
    #description_template = 'feeds/comment_feed.html'
    #description_template = 'feeds/comment_feed.html'
    #turbo_sanitize = True
    
    def items(self):
        return Qs.objects.all().filter(active__exact=True).filter(created__lte=timezone.now()).order_by('-created').all()  
    #def get_object(self, request,**kwargs):
        #return Section.objects.get(<slug:razdel_slug>/<slug:slug>pk=beat_id)

    def item_title(self, item):
        return "%s тема " % item.theme

    #def link(self, item):
        #return item.get_absolute_url()

    def item_turbo(self, item):
        return 'Вопрос: "{}" ( {} ) Ответ: {} '.format(truncatewords_html(item.main,50),item.theme, truncatewords_html(item.reply,50))    



