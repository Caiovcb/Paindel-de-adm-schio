from django.contrib import admin
from dadoste.formulario.models import Formularios


@admin.register(Formularios)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'cliente', 'nome']
    search_fields = [
        'nome',
        "tipo__nome",
        "cliente__nome",
    ]
