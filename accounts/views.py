from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomSignUp

class SignUp(generic.CreateView):
    form_class = CustomSignUp
    
    success_url = reverse_lazy('login')



    template_name = 'registration/register.html'
    

def reset(request):
    return render(request,'registration/')
        