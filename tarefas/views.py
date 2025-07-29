from django.shortcuts import redirect, render,get_object_or_404
from .models import Tarefas
from django.contrib.auth.decorators import login_required
from .forms import TarefaForm
from django.conf import settings

def sua_view(request):
    context = {
        'logo_preta': settings.LOGO_PRETA,
        'logo_vermelho': settings.LOGO_VERMELHO
    }
    return render(request, 'login.html', context)


# função da pagina OverView
@login_required
def overlist(request):
    tarefas = Tarefas.objects.all()

    search = request.GET.get('search')
    status = request.GET.get('status')
    categoria = request.GET.get('categoria')

    if search:
        tarefas = tarefas.filter(titulo__icontains=search)

    if status:
        tarefas = tarefas.filter(status__icontains=status)

    if categoria:
        tarefas = tarefas.filter(categoria__icontains=categoria)


    
    tarefas = tarefas.order_by('-created_at')
    
        
    context = {
        'tarefas': tarefas,
        'search' : search,
        'status' : status,
        'categoria' : categoria,
        'total_tf': tarefas.count()

        
    }
    
    
    return render(request, 'tarefas/overview.html', context)



# renderia as listagem de tarefas filtrada pelo usuario logado
@login_required
def listaTarefas(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at').filter(usuario=request.use,profile=None)
    search = request.GET.get('search')
    if search:
        tarefas = Tarefas.objects.filter(titulo__icontains=search, usuario=request.user)
        return render(request,'tarefas/list.html',{'tarefas':tarefas})
    else:
        return render(request,'tarefas/list.html',{'tarefas':tarefas_list})


# função Nova Tarefa - para criar uma nova tarefa
@login_required
def novaTarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

    
        if form.is_valid:
            tf = form.save(commit=False)
            tf.usuario = request.user

            tf.save()
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