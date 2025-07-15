from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.listaTarefas,name='Listagem'),
    path('novaTarefa/', views.novaTarefa, name='NovaTarefa'),
    path('tarefa/<int:id>/',views.tarefaView, name='TarefaView'),
    path('editar/<int:id>/', views.editarTarefa, name='EditarTarefa'),
    path('delete/<int:id>/', views.deleteTarefa, name='DeleteTarefa')
]
