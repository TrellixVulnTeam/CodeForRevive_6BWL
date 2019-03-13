from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'manager'

urlpatterns = [path('', views.LoginPage, name="login"),
               path('signup/', views.signUpPage, name="signup"),
               path('welcome/', views.welcomePage, name="welcomepage"), ]
