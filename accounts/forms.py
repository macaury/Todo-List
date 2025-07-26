from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomSignUp(UserCreationForm):
      email = forms.EmailField(required=True,label='E-mail')
      first_name= forms.CharField(required=True,label='Nome')
      last_name = forms.CharField(required=True,label='Sobrenome')
      
      class meta:
            models = User
            fields = (
                  'username',
                  'first_name',
                  'last-name',
                  'email',
                  'password1',
                  'password2'
            )
            
      
      def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                  raise forms.ValidationError("Este e-mail já está em uso.")
            return email