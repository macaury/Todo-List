from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

from .forms import CustomSignUp

class SignUp(generic.CreateView):
    form_class = CustomSignUp
    success_url = reverse_lazy('login')
    #template_name = 'registration/register.html'
    template_name = 'registration/novo_register.html'
    



class Config_interface():
    def __init__(self):
        pass
        