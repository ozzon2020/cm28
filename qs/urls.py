from django.urls import path
from . import views
from .feeds import YQuestionsFeed


app_name = 'qs'

urlpatterns = [
    path('', views.QsListView.as_view(), name='questions-detail'),
    path('post/<int:pk>', views.QsDetailView.as_view(), name='qs-detail'),
    path('create/',views.QsCreateView.as_view(),name='qs_create'),   
    path('edit/<int:pk>',views.QsUpdateView.as_view(),name='qs_edit'),    
    path('feeds/', YQuestionsFeed(), name='qs_feed'),  

] 