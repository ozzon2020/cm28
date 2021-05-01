from django.views import generic
#from django.shortcuts import render
from qs.models import Qs,ThemeQs
from content.models import Razdel, Block
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView,FormMixin
from django.utils import timezone
from django.utils.timezone import now
from django.urls import  reverse,reverse_lazy
from qs.forms import  QsForm,ReplyForm
from django.shortcuts import render,get_object_or_404  
#from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from actions.utils import create_action
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
#from django.http import JsonResponse
#from django.views.decorators.http import require_POST
#from common.decorators import ajax_required
#from hitcount.views import HitCountDetailView

##  from haystack.query import SearchQuerySet
## from haystack.generic_views import SearchView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
#from .models import Tag, TaggedItem
#from django.views.generic.base import ContextMixin
#from common.menumixin import MenuMixin


class QsUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    
    
    permission_required = 'questions.change_qs'
    model = Qs

    fields = ['reply',]
    def form_valid(self, form):

        
        success_message = '<div class="header">Ответ опубликован </div> <p>Спасибо за Вашу отзывчивость.</p>'
        messages.success(self.request, success_message)
        return super().form_valid(form)
    
    success_url =reverse_lazy('qs:questions-detail')  
    

class QsCreateView(CreateView):
    model = Qs
    #form_class = QsForm
    #fields = ('title', 'description')
    fields = ('var','theme','name','email','main',)   
    
    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            get_recaptcha = request.POST.get("g-recaptcha-response")
            return self.form_valid(form)
        else:
            success_message = '<div class="header">Ваш вопрос не добавлен</div> <p>Вы не правильно заполнили форму. Проверьте пожалуйста...</p>'
            messages.error(self.request, success_message)
            return self.form_invalid(form)            
            #return HttpResponseRedirect("/qs/")
        
    def form_valid(self, form):
        create_action(form.cleaned_data['name'], 'Вопрос врачу '+form.cleaned_data['theme'],'user md')
        
        var=form.cleaned_data['var'],
        theme=form.cleaned_data['theme'],
        #direction=form.cleaned_data['direction'],
        name=form.cleaned_data['name'],
        email=form.cleaned_data['email'],
        main=form.cleaned_data['main'],       
        success_message = '<div class="header">Вопрос опубликован </div> <p>Спасибо за Ваш интерес.</p>'
        messages.success(self.request, success_message)
        return super().form_valid(form)
    
    success_url =reverse_lazy('qs:questions-detail')
    
  
    
class QsListView(FormMixin,generic.ListView):
    model = Qs
    paginate_by = 10
    #form = SearchForm()
    form_class = QsForm
    
    template_name = 'qs/qs-list.html'
    qssave=''
    #t=''
    #let=()
    #num=()
    #let1=()
    #num1=()
    
    #tags =Tag.objects.all()
    #tags('apple','apple2','apple3','apple4')
    #for tag in tags:
        #co=Qs.objects.filter(active__exact=True).filter(created__lte=timezone.now()).filter(tags__name__in=[tag.name]).count()
        
        ##let1(str(tag),)
        #if co > 0 and tag.slug !='':
            #let=let+(tag,)
        ##num1=(co,)
            #num=num+(co,)
    
    #t = list(zip(let,num))

    def get_success_url(self):
        pk = self.kwargs['pk']
        self.object = self.get_object()
        #create_action(self.request.user, 'Вопрос врачу','user md',self.object.__dict__)
        
        return reverse_lazy('qs:questions-detail')
    
    def get_queryset(self):
        return self.model.objects.filter(active__exact=True).filter(created__lte=timezone.now()).all() 

    

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['form_reply'] = ReplyForm()
        #context['tag_list']=self.t
        context['qs_item']=True
        context['page'] =self.request.GET.get('page')
        context['sloganheader']=  '<h1>Вопрос / Ответ на  28cm.ru</h1><p>Задайте инитересующий Вас вопрос и квалифицированный специалист ответит на него</p>'
        context['leftblock']=Block.objects.get(slug__exact='leftblock')
        context['leftblock2']=Block.objects.get(slug__exact='leftblock2')
        #context['image_top'] ='hf043.jpg'
        #context['image_bot'] ='hf018.jpg'        
        return context    
    
class QsDetailView(generic.DetailView):
    model = Qs 
    template_name = 'qs/qs.html'
    #count_hit = True

    #Post.objects.filter(tags__name__in=["python"]).count()
    
    def get_success_url(self):
        #pk = self.kwargs['pk']
        return reverse_lazy('qs:qs-detail', kwargs={'pk': self.object.pk})    
    

    
    def get_queryset(self):
        return self.model.objects.filter(active__exact=True).filter(created__lte=timezone.now()) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #context['menu'] = Razdel.objects.filter(active__exact=1).all()
        #context['results'] =results
        context['page'] =self.request.GET.get('page')
        context['qs_item']=True
        context['sloganheader']=  '<h1>  Тема : '+self.object.var.name+'</h1><p>Вопрос / Ответ на 28cm.ru - '+self.object.theme+'</p>'


        return context       