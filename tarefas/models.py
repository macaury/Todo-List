from django.db import models
from django.contrib.auth import get_user_model

class Tarefas(models.Model):
    titulo = models.CharField(max_length=254)
    descricao = models.TextField()
    usuario = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    #categoria_tarefa= models.CharField(max_length=20)
    #data_finalizacao = models.DateField(None)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.titulo)
