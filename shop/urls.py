from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.home,name='home'),
    path('tovary', views.product_list, name='product_list'),
    path('tovary/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('tovary/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
