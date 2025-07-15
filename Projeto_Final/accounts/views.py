from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserChangeForm
    sucess_url = reverse_lazy('login')
    template_name = 'registration/register.html'

