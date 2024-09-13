from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .models import Tarefa
from .forms import TarefaForm, CustomUserCreationForm

#Função para criar novo usuário
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('listar_tarefas')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tarefas/signup.html', {'form': form})

#Função para criar nova tarefa
@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.atribuido_a = request.user
            tarefa.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/criar_tarefa.html', {'form': form})

#Função para editar tarefa existente
@login_required
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if tarefa.atribuido_a != request.user:
        return redirect('listar_tarefas')

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    
    return render(request, 'tarefas/editar_tarefa.html', {'form': form})

#Função para listar as tarefas do usuário
@login_required
def listar_tarefas(request):
    status_filter = request.GET.get('status', None)
    search_query = request.GET.get('search', '')

    tarefas = Tarefa.objects.filter(
        titulo__icontains=search_query
    )

    if status_filter:
        tarefas = tarefas.filter(status=status_filter)

    tarefas = tarefas.filter(atribuido_a=request.user)

    return render(request, 'tarefas/listar_tarefas.html', {
        'tarefas': tarefas,
        'search_query': search_query,
    })

#Função para excluir tarefa
@login_required
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if tarefa.atribuido_a != request.user:
        return redirect('listar_tarefas')

    if request.method == 'POST':
        tarefa.delete()
        return redirect('listar_tarefas')

    return render(request, 'tarefas/excluir_tarefa.html', {'tarefa': tarefa})