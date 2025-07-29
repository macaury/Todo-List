from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    # Relação 1-para-1 com o modelo User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
        
    email = models.EmailField(max_length=30)
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
      
    data_nascimento = models.DateField( null=True,blank=True)
    
    def clean_email(self):
            email = self.cleaned_data.get('email')
            print(email)
            if User.objects.filter(email=email).exists():
                  raise models.ValidationError("Este e-mail já está em uso.")
            return email
    
    def __str__(self):
        return self.user.username

# Sinais para criar/atualizar o Profile automaticamente
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()