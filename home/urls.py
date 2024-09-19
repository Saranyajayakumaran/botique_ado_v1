
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('clear-cache/', views.clear_cache, name='clear_cache'),
]
    
