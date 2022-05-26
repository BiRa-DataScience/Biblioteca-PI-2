from django.contrib import admin

from .models import Material, Aluno


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material', 'titulo', 'autor', 'data', 'armario', 'prateleira', 'posse', 'dataposse')
    search_fields = ('titulo', 'autor', 'posse', 'dataposse')
    list_filter = ('titulo',)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'documento', 'divisao', 'email', 'data')
