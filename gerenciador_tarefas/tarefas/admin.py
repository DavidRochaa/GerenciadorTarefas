from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'status', 'criado_em', 'atribuido_a') #Campos que são exibidos
    list_filter = ('status', 'criado_em') #Filtros de busca
    search_fields = ('titulo', 'descricao')  #Campos de busca

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(atribuido_a=request.user)