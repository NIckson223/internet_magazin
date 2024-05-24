from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('subscribers', views.subs, name='subs'),
    path('mostpopular',views.most_popular, name='most_popular'),
    path('last25',views.last_25, name='last_25'),
    path('type',views.type, name='type'),
    path('most_popular_25',views.most_popular_25, name='most_popular_25'),
    path('popular',views.popular, name='popular'),
]
