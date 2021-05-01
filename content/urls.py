from django.urls import path
#from django.views.generic import RedirectView
from . import views
from content.feeds import YTurboFeed

    #feed = TurboFeed()

app_name = 'content'

urlpatterns = [
    #path('', views.IndexDetailView.as_view(),name='index'),
    #path('post/contact', views.ContactView.as_view(), name='post_contact'),
    path('', views.index,name='index'),
    #path('login/', views.login,name='login_index'),
    path('page/<slug:slug>/', views.SectionDetailView.as_view(), name='section-detail'),
    path('tag/<slug:tag_slug>/',views.TagListView.as_view(), name='section_list_by_tag'),    
    path('robots.txt',views.robots,name='robots'),
    
    #path('contentfeed/', ContentFeed(), name='content_feed'),
    #path('commentfeed/', YCommentFeed(), name='comment_feed'),
    path('turbo_content/', YTurboFeed(), name='turbo_content'),

]
