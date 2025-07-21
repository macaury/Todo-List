from django.shortcuts import redirect, render,get_object_or_404
from .models import Tarefas

from django.contrib.auth.decorators import login_required

from .forms import TarefaForm

import pandas as pd 
from plotly.offline import plot
import plotly.express as px


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
    tarefas = Tarefas.objects.filter(usuario=request.user)
    # Gráfico de tarefas por dia
    df = pd.DataFrame(tarefas.values('created_at'))
    df['data'] = pd.to_datetime(df['created_at']).dt.date
    
    if not df.empty:
        fig = px.bar(
            df.groupby('data').size().reset_index(name='count'),
            x='data',
            y='count',
            title='Tarefas Criadas por Dia'
        )
        plot_div = plot(fig, output_type='div', config={'displayModeBar': False})
    else:
        plot_div = "<p>Sem dados para exibir</p>"
    
    context = {
        'tarefas': tarefas.order_by('-created_at'),
        'total_tarefas': tarefas.count(),
        'plot_tarefas': plot_div
    }

    
    
    return render(request, 'tarefas/overview.html', context)
#def overlist(request):
# 
#    tarefas = Tarefas.objects.all()
#    df = pd.DataFrame(list(tarefas.values()))
#    
#    tarefas_list = tarefas.order_by('-created_at')
#
#    search = request.GET.get('search')
#
#    total = len(tarefas)
#
#    context = {
#        'tarefas':tarefas,
#       'total': total
#    }
#  
#    if search:
#        tarefas = Tarefas.objects.filter(titulo__icontains=search, usuario=request.user)
#        return render(request,'tarefas/overview.html',context)
#    else:
#        return render(request,'tarefas/overview.html',context) # {'tarefas':tarefas_list}

@login_required
def filtro_categoria(request):

    status_filter = request.GET.get('status')
    categoria_filter = request.GET.get('categoria')

    tarefas = Tarefas.objects.filter(usuario=request.user).order_by('-created_at')

    if status_filter:
        tarefas = tarefas.filter(status__icontains=status_filter)

    if categoria_filter:
        tarefas = tarefas.filter(categoria__icontains=categoria_filter)

    context = {
        'tarefas': tarefas,
        'status_choices': Tarefas.status_list,
        'categoria_choices': Tarefas.categoria_list,
        'status_selecionado': status_filter,
        'categoria_selecionada': categoria_filter
    }

    return render(request, 'overview.html', context)

# renderia as listagem de tarefas filtrada pelo usuario logado
@login_required
def listaTarefas(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at').filter(usuario=request.user)
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