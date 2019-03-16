from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'manager'

urlpatterns = [path('', views.loginPage, name="login"),
               path('signup/', views.signUpPage, name="signup"),
               path('welcome/$', views.welcomePage, name="welcomepage"),
               # path('invitations/', include('invitations.urls', namespace='invitations')),
               path('welcome/createteams/', views.createTeam, name="createTeams"),
               path('createteams/(?<pk>\d)', views.TeamListView.as_view(), name= "TeamList"),


    ]
