"""prep_su URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from common.sitemaps import ContentSitemap,HomeSitemap,QsSitemap,ShopSitemap,CategorySitemap,TagSitemap
from django.urls import  reverse,reverse_lazy 

handler404 = 'content.views.handler404'
handler403 = 'content.views.handler403'

sitemaps = {
    'home': HomeSitemap,
    #'direction': DirectionSitemap,
    #'razdel': RazdelSitemap,
    'tag':TagSitemap,
    'sections': ContentSitemap,
    'qs':QsSitemap,
    'category':CategorySitemap,
    'shop':ShopSitemap

    
}



urlpatterns = [
    path('', include('content.urls')),
    path('catalog/', include('shop.urls', namespace='shop')),
    path('postdoctor/', include('qs.urls', namespace='qs')),
    path('search/result/', include('haystack.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('summernote/', include('django_summernote.urls')),
    
]

if settings.DEBUG:
    #urlpatterns += path('summernote/', include('django_summernote.urls'))
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
