from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:number>/',views.detail,name='detail'),
    path('<int:number>/favorite',views.favorite,name='favorite'),
]



