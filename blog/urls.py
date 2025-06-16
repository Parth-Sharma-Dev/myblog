from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post, name='post'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
