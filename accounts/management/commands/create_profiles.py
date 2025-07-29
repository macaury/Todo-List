# SuaApp/management/commands/create_profiles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import Profile

class Command(BaseCommand):
    help = 'Cria perfis para usuários que ainda não têm'

    def handle(self, *args, **options):
        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
                self.stdout.write(f'Perfil criado para {user.username}')
        self.stdout.write(self.style.SUCCESS('Todos os perfis foram criados!'))