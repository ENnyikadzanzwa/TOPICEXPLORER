from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('content/', views.Content, name='content'),
    path('question/', views.Question, name='question'),
    path('evaluation/', views.Evaluation, name='evaluation'),
    path('help/', views.help, name='help'),
   

]