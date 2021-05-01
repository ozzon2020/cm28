from content.models import Razdel, Section, Chast
from shop.models import MedRazdel,Category,Product
from django.utils import timezone
from django.db.models import Q

#from actions.models import Action
#from actions.utils import create_action

#def push_menu(request):
    ##createnow=timezone.now()
    #push_menu = Razdel.objects.filter(active__exact=True).exclude(namefile__in=['all','page',]).all()    
    ##Two_menu = Razdel.objects.filter(active__exact=True).filter(id__in=[24,]).all()
    #return {'push_menu': push_menu,'createnow':timezone.now()}
def main_menu(request):
    #menu_page = Razdel.objects.filter(active__exact=True).exclude(namefile__in=['allpage',]).filter(created__lte=timezone.now()).all()
    #menu_page = Razdel.objects.filter(namefile__exact='page').filter(active__exact=True).filter(created__lte=timezone.now()).all()
    #.extra(select={'is_recent': "pub_date > '2006-01-01'"})
    menu_page = Razdel.objects.filter(namefile__in=['page',]).filter(active__exact=True).filter(created__lte=timezone.now()).all()
    products = Product.objects.filter(active__exact=True).filter(created__lte=timezone.now()).all()
    #desctop_menu_page = Chast.objects.filter(var__exact=1).filter(active__exact=True).filter(chrazdel__created__lte=timezone.now())
    desctop_menu_page = Chast.objects.filter(var__exact=1).filter(active__exact=True).all()
    menu_product = MedRazdel.objects.filter(active__exact=True).filter(created__lte=timezone.now()).all()
    #menu_page = Razdel.objects.filter(Q(namefile='page') & Q(active=1)).all()
    #menu_page = Razdel.objects.extra(select={'content_razdel': "namefile == 'page'"}).filter(active__exact=True).filter(created__lte=timezone.now()).all()
    #main_menu = Razdel.objects.filter(active__exact=True).exclude(namefile__in=['allpage',]).all()[0:5]    
    #two_menu = Razdel.objects.filter(active__exact=True).filter(namefile__in=['product',]).all()
    razdel_menu = Razdel.objects.exclude(namefile__in=['page',]).filter(active__exact=True).filter(created__lte=timezone.now()).order_by('-sort')
    return {'menu_page': menu_page,
            'desctop_menu_page':desctop_menu_page,
            'products':products,
            'menu_product':menu_product,
            'createnow':timezone.now()} 


