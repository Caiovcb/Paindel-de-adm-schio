from django.contrib import admin
from Formulario.models import Formularios


@admin.register(Formularios)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'cliente', 'fornecedor', 'nome']
    search_fields = [
        'nome',
        "tipo__nome",
        "cliente__nome",
        "fornecedor__nome",
    ]
