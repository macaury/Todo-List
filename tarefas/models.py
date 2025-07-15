from django.db import models

class Tarefas(models.Model):
    titulo = models.CharField(max_length=254)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
