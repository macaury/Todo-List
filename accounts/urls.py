from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='signup'),
    path('reset-pass/', views.reset, name='reset'),
    

  
   # path('configuracao/', views.configuracao, name='configuracao')

    ]