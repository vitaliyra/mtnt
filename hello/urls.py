from django.contrib import admin
#from django.urls import path
from firstapp import views
from django.conf.urls import include, url
 
urlpatterns = [
    url('', views.index),
]