from django import template
from shop.models import Review
from django.utils import timezone
from django.db.models import Sum


register = template.Library()

@register.simple_tag
def total_review(spk):
    #spk = kwargs['section_pk']
    #return Comment.active.count()
    return Review.objects.filter(active__exact=True).filter(product__exact=spk).filter(created__lte=timezone.now()).count()

@register.simple_tag
def total_raiting(spk):
    count_raiting=Review.objects.filter(active__exact=True).filter(product__exact=spk).filter(created__lte=timezone.now()).count()
    summa_raiting=Review.objects.filter(active__exact=True).filter(product__exact=spk).filter(created__lte=timezone.now()).all().aggregate(Sum('rating'))
    if(count_raiting==0 or summa_raiting==0):
        fin_raiting=0
    else:
        fin_raiting=round(float(summa_raiting['rating__sum']) / float(count_raiting) , 2)   
    #fin_raiting=float(summa_raiting['rating__sum']) / float(count_raiting)
    #spk = kwargs['section_pk']
    #return Comment.active.count()
    return fin_raiting