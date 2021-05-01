from django.views import generic
from django.views.generic.base import ContextMixin
from content.models import Razdel,Section,Chast
from django.utils import timezone

class MenuMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        
        #context['popular_comments'] = Comment.objects.filter(active__exact=True).filter(created__lte=timezone.now()).order_by('-total_likes')[0:3]
        context["menu_page"] = Razdel.objects.filter(active__exact=True).all()
        #context['menu_page'] = Razdel.objects.filter(active__exact=True).filter(sectionrazdel=self.object).all()
        #context['razdel_menu'] = Razdel.objects.exclude(namefile__in=['page',]).filter(active__exact=True).filter(created__lte=timezone.now()).order_by('-sort')
        
        return context