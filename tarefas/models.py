from django.db import models
from django.contrib.auth import get_user_model

class Tarefas(models.Model):

    sprint_semanal = 'sprint semanal'
    sprint_quinzenal = 'sprint quinzenal'
    sprint_mensal = 'sprint mensal'
    sprint_anual = 'sprint anual'

    status_1 = 'aberto'
    status_2 = 'standby'
    status_3 = 'andamento'
    status_4 = 'finalizado'

    categoria_list = [(sprint_semanal ,'sprint semanal'),(sprint_quinzenal ,'sprint quinzenal'),(sprint_mensal ,'sprint mensal'),(sprint_anual ,'sprint anual')]

    status_list = [(status_1,'aberto'),(status_3,'andamento'),(status_2,'standby'),(status_4,'finalizado')]

    usuario = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    descricao = models.TextField(blank=False,max_length=254)
    categoria= models.CharField(max_length=20,choices=categoria_list,default=sprint_semanal)
    status= models.CharField(max_length=18,choices=status_list,default=status_1)
    #data_finalizacao = models.CharField(d)
   


    #campo de status da tarefa

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (self.titulo)
