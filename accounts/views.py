from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomSignUp

  
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class SignUp(generic.CreateView):
    form_class = CustomSignUp
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    
    
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    email_template_name = 'registration/reset_password_email.html'
    subject_template_name = 'registration/password_reset_subject'
    success_message = "O email foi enviado com sucesso"
    
    success_url = reverse_lazy('login')

        