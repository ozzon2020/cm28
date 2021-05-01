from django.urls import path
from . import views
from shop.feeds import YTurboCategory,YTurboProduct

app_name = 'shop'

urlpatterns = [
    path('payment/',views.payment,name='payment'),
    #path('shopfeed/', YShopFeed(), name='shop_feed'),

    path('', views.MedRazdelDetailView.as_view(),name='razdel-list'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('items/', YTurboCategory(), name='сategory-product'),
    path('items/product/', YTurboProduct(), name='product'),
    
    #path('', views.CategoryDetailView.as_view(),name='product_list'),
    path('<slug:slug>/', views.CategoryDetailView.as_view(),name='category-list'),


    path('add/<int:product_id>/',views.cart_add,name='cart_add'),
    path('remove/<int:product_id>/',views.cart_remove, name='cart_remove'),
    path('order/create/', views.order_create, name='order_create'),

    #path('like/', views.review_like, name='like'),
    #path('dislike/', views.review_dislike, name='dislike'),

    #path('<slug:category_slug>/', views.CategoryDetailView.as_view(),name='product_list_by_category'),

    #path('product/<int:id>/<slug:slug>', views.ProductDetailView.as_view(),name='product_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.ProductDetailView.as_view(),name='product_detail'),
    path('admin/order/<int:order_id>/pdf/',views.admin_order_pdf,name='admin_order_pdf'),
    
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    


] 