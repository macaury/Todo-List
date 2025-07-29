from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class CustomSignUp(UserCreationForm):
  
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


      def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            Profile.objects.update_or_create(
                  user=user,
                  defaults={'nome':self.clean.get('nome','')}
            )
            
        return user

            