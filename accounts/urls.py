from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='signup'),
  
     path('password_reset/', views.PasswordResetView.as_view(template_name='registration/reset_password_email.html'),name='password_reset'),
  
        
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_complete'),
    
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
    
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html' ), name='password_reset_confirm'),
    
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html') , name='password_reset_complete')
    
    
    ]