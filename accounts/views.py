from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomSignUp

  

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class SignUp(generic.CreateView):
    form_class = CustomSignUp
    
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    
    
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):

    template_name = 'registration/reset_password.html'
    email_template_name = 'registration/email/reset_password_email.html'
    subject_template_name = ''
    success_message = "O email foi enviado com sucesso"
    
    success_url = reverse_lazy('login')

def change_password(request):
    return render(request,'registration/change_password')


def reset(request):
    return render(request,'registration/reset_password.html')
        