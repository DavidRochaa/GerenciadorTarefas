from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('listar/', views.listar_tarefas, name='listar_tarefas'),
    path('editar/<int:pk>/', views.editar_tarefa, name='editar_tarefa'),
    path('excluir/<int:pk>/', views.excluir_tarefa, name='excluir_tarefa'),
]
