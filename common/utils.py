from django.conf import settings
#from django.contrib.staticfiles.templatetags.staticfiles import static
from django_summernote.widgets import SummernoteWidget,SummernoteInplaceWidget
from django.urls import  reverse
from django.templatetags.static import static
#from bs4 import BeautifulSoup
import textwrap
from django.utils.html import strip_tags
import re
from rutermextract import TermExtractor
from razdel import sentenize



class SummernoteWidgetWithCustomToolbar(SummernoteInplaceWidget):
    def summernote_settings(self):
        summernote_config=settings.SUMMERNOTE_CONFIG
        summernote_settings = summernote_config.get('summernote', {}).copy()
        lang = summernote_config['summernote'].get('lang')
        
        summernote_settings.update({
            'lang': lang,
            'width' : '100% ',
            'height': '200',
            'codeviewFilter': 'false',
            'codeviewIframeFilter': 'true',
            #'dialogsInBody': 'false',
            #'dialogsFade': 'true',
            'url': {
                'language': static('summernote/lang/summernote-' + lang + '.min.js'),
                'upload_attachment': reverse('django_summernote-upload_attachment'),
                },
            'toolbar': [
                #['style', ['style', ]],
                ['font', ['bold', 'italic', 'underline','clear']],
                ['misc', ['undo', 'redo',]],
               
                ],
          
        })
        return summernote_settings 
    
    
def make_desc_title(self, request, queryset):
    
    idf = dict()
    term_extractor = TermExtractor()
    
    for obj in queryset:
        #val1=strip_tags(obj.main)
        keyword=''
        stattext=''
        descripshion=''
        descripshion_stat=''
        mytags=''
        count_tags=0
        ttext=''

        count_word=len(set(strip_tags(obj.main).split()))
        
        kw=[]
        
        for term in term_extractor(strip_tags(obj.main),10, weight=lambda term: idf.get(term.normalized, 1.0) * term.count):
            stattext+=term.normalized+'  :'+str(term.count)+' тошнота- '+str(float('{:.2f}'.format(term.count/count_word*100*7)))+'%\n'
            kw.append(term.normalized)
            keyword+=term.normalized+','
            if count_tags < 5:
                mytags+=term.normalized+','
                count_tags=count_tags+1
                     
        text_page=list(sentenize(re.sub('\n', ".", (re.sub('\n+', "", strip_tags(obj.main))))))
        
        i=0
        
        for t in text_page:
            #terms = TermExtractor()
            for term in term_extractor(t.text):
                
                if re.search(kw[i],term.normalized):

                
                    if len(kw) > i:
                        input1 = re.sub('\n+', " ",  t.text)
                        input1 = re.sub('\[[0-9]*\]', "", input1)
                        input1 = re.sub('&nbsp;', " ", input1)
                        input1 = re.sub(' +', " ", input1)                        
                        descripshion+=input1
                        descripshion_stat+=descripshion+' ( '+kw[i]+' )  ['+str(len(kw)-i)+'] '
                        if t.text != '':
                            ttext+=t.text+' (-- '+kw[i]+' )\n'
                    i+=1
                #if len(kw) > i   and  t.start > 1000 :
                    ##circle_txt(text_a[0:],W,F,i)
                    for t in text_page:
                        try:
                            if re.search(kw[i],term.normalized):
                                if len(kw) > i:
                                    descripshion+=re.sub(' +', " ", t.text)
                                    descripshion_stat+=descripshion+' ( '+kw[i]+' )  ['+str(len(kw)-i)+'] '
                                    ttext=t.text
                                i+=1  
                        except IndexError:
                            i=1

        #obj.tags = TaggableManager(through=RuTaggedItem)                    
        obj.title=textwrap.shorten(re.sub('&nbsp;', "",  strip_tags(obj.main)), width=150, placeholder="")
        obj.meta_description=textwrap.shorten(re.sub('&nbsp;', "",descripshion), width=248, placeholder="")
        #obj.stattext='Всего слов: '+str(count_word)+'\n'+stattext+'\n--------------------\n'+descripshion_stat+'\n\n'+ttext
        obj.stattext='Всего слов: '+str(count_word)+'\n Титл:\n'+ \
        obj.title+'\n------------------------\nDescription:\n'+obj.meta_description+'\n-------------------- \n' +\
        stattext+'\n--------------------\n'+mytags+'\n\n'+ttext
        
        obj.meta_keywords=textwrap.shorten(keyword,width=248)
        #obj.save(commit=False)
        #obj.tags=mytags
        #obj.save_m2m(['tags'])
        #obj.save(update_fields=(['meta_keywords','title','meta_description','stattext']))
        obj.save(update_fields=(['title','meta_keywords','meta_description','stattext',]))
       
    self.message_user(request, "Заголовок страницы изменен "+str(count_word)) 
    
def make_product_title(self, request, queryset):
    
    idf = dict()
    term_extractor = TermExtractor()
    
    
    for obj in queryset:
        #val1=strip_tags(obj.main)
        keyword=''
        stattext=''
        descripshion=''
        descripshion_stat=''
        mytags=''
        count_tags=0
        ttext=''
        
        main=obj.about+obj.description+obj.priem+obj.sostav+obj.kurs+obj.izgotovitel
        count_word=len(set(strip_tags(main).split()))
        
        kw=[]
   
        for term in term_extractor(strip_tags(main),10, weight=lambda term: idf.get(term.normalized, 1.0) * term.count):
            stattext+=term.normalized+'  :'+str(term.count)+' тошнота- '+str(float('{:.2f}'.format(term.count/count_word*100*7)))+'%\n'
            kw.append(term.normalized)
            keyword+=term.normalized+','
            if count_tags < 5:
                mytags+=term.normalized+','
                count_tags=count_tags+1
                     
        text_page=list(sentenize(re.sub('\n', ".", (re.sub('\n+', "", strip_tags(main))))))
        
        i=0
        
        for t in text_page:
            #terms = TermExtractor()
            for term in term_extractor(t.text):
                
                if re.search(kw[i],term.normalized):

                
                    if len(kw) > i:
                        input1 = re.sub('\n+', " ",  t.text)
                        input1 = re.sub('\[[0-9]*\]', "", input1)
                        input1 = re.sub('&nbsp;', " ", input1)
                        input1 = re.sub(' +', " ", input1)                        
                        descripshion+=input1
                        descripshion_stat+=descripshion+' ( '+kw[i]+' )  ['+str(len(kw)-i)+'] '
                        if t.text != '':
                            ttext+=t.text+' (-- '+kw[i]+' )\n'
                    i+=1
                #if len(kw) > i   and  t.start > 1000 :
                    ##circle_txt(text_a[0:],W,F,i)
                    for t in text_page:
                        try:
                            if re.search(kw[i],term.normalized):
                                if len(kw) > i:
                                    descripshion+=re.sub(' +', " ", t.text)
                                    descripshion_stat+=descripshion+' ( '+kw[i]+' )  ['+str(len(kw)-i)+'] '
                                    ttext=t.text
                                i+=1  
                        except IndexError:
                            i=1
                
        obj.title=textwrap.shorten(re.sub('&nbsp;', "",  strip_tags(main)), width=150, placeholder="")
        obj.meta_description=textwrap.shorten(re.sub('&nbsp;', "",descripshion), width=248, placeholder="")
        #obj.stattext='Всего слов: '+str(count_word)+'\n'+stattext+'\n--------------------\n'+descripshion_stat+'\n\n'+ttext
        obj.stattext='Всего слов: '+str(count_word)+'\n Титл:\n'+ \
        obj.title+'\n------------------------\nDescription:\n'+obj.meta_description+'\n-------------------- \n' +\
        stattext+'\n--------------------\n'+mytags+'\n\n'+ttext
        
        obj.meta_keywords=textwrap.shorten(keyword,width=248)

        obj.save(update_fields=(['meta_keywords','title','meta_description','stattext']))
        #obj.save(update_fields=(['meta_keywords','meta_description','stattext',]))
        #obj.save(update_fields=(['stattext',]))
       
    self.message_user(request, "Заголовок страницы изменен "+str(count_word)) 
    
def make_category_product(self, request, queryset):
    
    idf = dict()
    term_extractor = TermExtractor()
    
    
    for obj in queryset:
        #val1=strip_tags(obj.main)
        keyword=''
        stattext=''
        descripshion=''
        descripshion_stat=''
        mytags=''
        count_tags=0
        ttext=''
        
        main=obj.description
        count_word=len(set(strip_tags(main).split()))
        
        kw=[]
   
        for term in term_extractor(strip_tags(main),10, weight=lambda term: idf.get(term.normalized, 1.0) * term.count):
            stattext+=term.normalized+'  :'+str(term.count)+' тошнота- '+str(float('{:.2f}'.format(term.count/count_word*100*7)))+'%\n'
            kw.append(term.normalized)
            keyword+=term.normalized+','
            if count_tags < 5:
                mytags+=term.normalized+','
                count_tags=count_tags+1
                     
        text_page=list(sentenize(re.sub('\n', ".", (re.sub('\n+', "", strip_tags(main))))))
        
        i=0
        
        for t in text_page:
            #terms = TermExtractor()
            for term in term_extractor(t.text):
                
                if re.search(kw[i],term.normalized):

                
                    if len(kw) > i:
                        input1 = re.sub('\n+', " ",  t.text)
                        input1 = re.sub('\[[0-9]*\]', "", input1)
                        input1 = re.sub('&nbsp;', " ", input1)
                        input1 = re.sub(' +', " ", input1)                        
                        descripshion+=input1
                        descripshion_stat+=descripshion+' ( '+kw[i]+' )  ['+str(len(kw)-i)+'] '
                        if t.text != '':
                            ttext+=t.text+' (-- '+kw[i]+' )\n'
                    i+=1
                #if len(kw) > i   and  t.start > 1000 :
                    ##circle_txt(text_a[0:],W,F,i)
                    for t in text_page:
                        try:
                            if re.search(kw[i],term.normalized):
                                if len(kw) > i:
                                    descripshion+=re.sub(' +', " ", t.text)
                                    descripshion_stat+=descripshion+' ( '+kw[i]+' )  ['+str(len(kw)-i)+'] '
                                    ttext=t.text
                                i+=1  
                        except IndexError:
                            i=1
                
        obj.title=textwrap.shorten(re.sub('&nbsp;', "",  strip_tags(main)), width=150, placeholder="")
        obj.meta_description=textwrap.shorten(re.sub('&nbsp;', "",descripshion), width=248, placeholder="")
        #obj.stattext='Всего слов: '+str(count_word)+'\n'+stattext+'\n--------------------\n'+descripshion_stat+'\n\n'+ttext
        obj.stattext='Всего слов: '+str(count_word)+'\n Титл:\n'+ \
        obj.title+'\n------------------------\nDescription:\n'+obj.meta_description+'\n-------------------- \n' +\
        stattext+'\n--------------------\n'+mytags+'\n\n'+ttext
        
        obj.meta_keywords=textwrap.shorten(keyword,width=248)

        obj.save(update_fields=(['meta_keywords','title','meta_description','stattext']))
        #obj.save(update_fields=(['meta_keywords','meta_description','stattext',]))
        #obj.save(update_fields=(['stattext',]))
       
    self.message_user(request, "Заголовок страницы изменен "+str(count_word))     
#def image_html_clean(body,size=''):
    #soup = BeautifulSoup(str(body), "html.parser")
    

    #whitelist = ['a','img']
    #for tag in soup.find_all(True):
        #if tag.name not in whitelist:
            #tag.attrs = {}
        #else:
            #attrs = dict(tag.attrs)
            #for attr in attrs:
                #if attr not in ['src','href']:
                    #del tag.attrs[attr] 
                    
    #for tag in soup.find_all('img'): 
        #attrs = dict(tag.attrs)
        #for attr in attrs:
            #if attr not in ['src','href']:
                #del tag.attrs[attr]
        #tag['class'] ='ui '+size+' floated image '
     
    #return str(soup)    