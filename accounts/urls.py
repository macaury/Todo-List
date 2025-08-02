from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='signup'),
  
    path('password-reset/', views.ResetPasswordView.as_view(template_name='registration/reset_password_email.html'), name='password_reset'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_email.html'),
         name='password_reset_complete'),
    ]