from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class CustomSignUp(UserCreationForm):
      email = forms.EmailField(max_length=30)
      first_name= forms.CharField(max_length=30)
      last_name = forms.CharField(max_length=30)
      
      team_code = forms.CharField(max_length=30)
      
      data_nascimento = forms.DateField()
      
      
      class meta:
            models = User
            fields = (
                  'username',
                  'first_name',
                  'last-name',
                  'email',
                  'password1',
                  'password2',
                  'data_nascimento',
                  'team_code'
            )


      def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            Profile.objects.update_or_create(
                  user=user,
                  defaults={'nome':self.clean.get('nome','')}
            )
            
        return user

            