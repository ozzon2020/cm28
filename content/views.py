from django.shortcuts import render
from django.views import generic
from content.models import Razdel,Chast,Section,Block
from shop.models import Product,Review,Category,MedRazdel
from qs.models import Qs
from django.urls import  reverse,reverse_lazy
from taggit.models import Tag, TaggedItem
from django.shortcuts import render,get_object_or_404  

from django.contrib import messages
#from common.menumixin import MenuMixin
import datetime
from django.utils import timezone
from django.utils.timezone import now



def handler404(request, exception):
    return render(request, 'error/404.html',  status=404)

def handler403(request, exception):
    return render(request, 'error/403.html', status=403)

def robots(request):
    return render(request, 'robots.txt')

def index(request):

    context = {
        #'block_index': Block.objects.filter(active__exact=True).order_by('-sort')[0:2],
        'main':get_object_or_404(Block,slug='index',active=True),
        #'indexplus':get_object_or_404(Block,slug='indexplus',active=True),
        'index_item':True,
        ##'new_comments':Comment.objects.filter(active__exact=1).filter(created__lte=timezone.now()).order_by('-created')[0:2],
        'medrazdel': MedRazdel.objects.filter(active__exact=True).all(),
        'section': Section.objects.filter(created__lte=timezone.now()).filter(active__exact=True).order_by('-created')[0:3],
        ##'popular_section' : Section.objects.filter(active__exact=True).filter(created__lte=timezone.now()).order_by('-hit_count_generic__hits')[0:2],
        'popular_questions' : Qs.objects.filter(active__exact=True).filter(created__lte=timezone.now()).order_by('-created')[0:3],
        'popular_product' : Product.objects.filter(active__exact=True).filter(created__lte=timezone.now()).order_by('-total_raiting')[0:4],


    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'content/index.html', context=context)


# Create your views here.
class SectionDetailView(generic.DetailView):
    model = Section 
    slug_field='namefile'
    template_name = 'content/section.html'
    #form_class = CommentForm
    #count_hit = True

    
    def get_success_url(self):
        #pk = self.kwargs['pk']
        return reverse_lazy('content:section-detail', kwargs={'slug': self.object.namefile})
    
    def get_queryset(self):
        return self.model.objects.filter(active__exact=True).filter(created__lte=timezone.now()).all()    

    

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_item']=True
        return context
  
class TagListView(generic.ListView):
    model = Section
    template_name = 'content/tags.html'
    paginate_by = 10
    tag = None 
    
   
    def get_queryset(self):
        #self.object_list = self.get_queryset()
        tag_slug = self.kwargs['tag_slug']
        try:
            self.tag = get_object_or_404(Tag, slug=tag_slug) 
            return self.model.objects.filter(active__exact=True).filter(tags__in=[self.tag]) 
    
        except Tag.DoesNotExist:
            return self.model.objects.filter(active__exact=True)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['section_item']=True
        context['leftblock']=Block.objects.get(slug__exact='leftblock')
        context['leftblock2']=Block.objects.get(slug__exact='leftblock2')
        #context['image_top'] ='hf043.jpg'        
        return context
