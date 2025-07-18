from django.db import models
from django.contrib.auth import get_user_model

class Tarefas(models.Model):

    sprint_semanal = 'sprint semanal'
    sprint_quinzenal = 'sprint quinzenal'
    sprint_mensal = 'sprint mensal'
    sprint_anual = 'sprint anual'

    status_Andamento = 'Em andamento'
    status_Procrastinando = 'Em procrastinação'
    status_Finalizado = 'Finalizado'
    status_Aberto = 'Em aberto'

    categoria_list = [(sprint_semanal ,'sprint semanal'),(sprint_quinzenal ,'sprint quinzenal'),(sprint_mensal ,'sprint mensal'),(sprint_anual ,'sprint anual')]

    status_list = [(status_Aberto,'Em aberto'),(status_Andamento,'Em andamento'),(status_Procrastinando,'Em procrastinação'),(status_Finalizado,'Finalizado')]

    usuario = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    titulo = models.CharField(max_length=254)
    descricao = models.TextField()
    categoria= models.CharField(max_length=20,choices=categoria_list,default=sprint_semanal)
    status= models.CharField(max_length=18,choices=status_list,default=status_Aberto)
    #data_finalizacao = models.CharField(d)
   


    #campo de status da tarefa

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.titulo)
