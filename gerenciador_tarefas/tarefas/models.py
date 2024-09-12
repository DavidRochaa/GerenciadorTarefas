from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    atribuido_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas', null=True, blank=True)

    def __str__(self):
        return self.titulo

    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, self.status)
