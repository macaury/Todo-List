from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class CustomSignUp(UserCreationForm):
      email = forms.EmailField(max_length=30)
      first_name= forms.CharField(max_length=30,label='primeiro nome')
      last_name = forms.CharField(max_length=30,label='segundo nome')
      #team_code = forms.CharField(max_length=30, required=None)
      class Meta:
            model = User
            fields = (
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
                  
            )

      print('ITEM AQUI 1')

      
      def save(self, commit=True):
        user = super().save(commit=False)
        
        
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
             
        if commit:
            user.save()
            print('ITEM AQUI 2')
            Profile.objects.update_or_create(
                  user=user
            )
            
        return user

      
      