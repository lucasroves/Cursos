from django.contrib import admin
from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'atualizacao', 'ativo']

@admin.register(Avaliacao)
class AvaliacaoAdmin (admin.ModelAdmin):
    list_display = ['curso','nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo']