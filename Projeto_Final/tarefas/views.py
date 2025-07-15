from django.shortcuts import redirect, render,get_object_or_404
from .models import Tarefas

from django.contrib.auth.decorators import login_required

from .forms import TarefaForm

# Create your views here.
@login_required
def listaTarefas(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')
    return render(request,'tarefas/list.html',{'tarefas':tarefas_list})


# função Nova Tarefa - para criar uma nova tarefa
@login_required
def novaTarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        form.save()
        return redirect('/')
    else:
        form = TarefaForm()
        return render(request,'tarefas/addTarefa.html',{'form':form})
    

# função Tarefa View - para ver detalhes de uma tarefa
@login_required
def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request,'tarefas/tarefaView.html',{'tarefa':tarefa})

# função Editar Tarefa - para editar uma tarefa existente
@login_required
def editarTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = TarefaForm(instance=tarefa)

    if(request.method == 'POST'):
        form = TarefaForm(request.POST, instance=tarefa)

        if (form.is_valid()):
            tarefa.save()
            return redirect('/')
        else: 
            return render(request,'tarefas/editTarefa.html',{'form':form, 'tarefa':tarefa})
    else: 
            return render(request,'tarefas/editTarefa.html',{'form':form, 'tarefa':tarefa})
    
# função Delete Tarefa - para deletar uma tarefa existente
@login_required
def deleteTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)

    tarefa.delete()
    return redirect('/')