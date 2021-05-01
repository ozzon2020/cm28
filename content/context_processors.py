from content.models import Razdel, Section
from django.utils import timezone

def main_menu(request):
    #createnow=timezone.now()
    Main_menu = Razdel.objects.filter(active__exact=True).exclude(namefile__in=['drug','about']).all()[0:5]    
    Two_menu = Razdel.objects.filter(active__exact=True).filter(id__in=[24,]).all()
    return {'Main_menu': Main_menu,'Two_menu':Two_menu,'createnow':timezone.now()}