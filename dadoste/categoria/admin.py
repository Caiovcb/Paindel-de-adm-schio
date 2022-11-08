from django.contrib import admin
from dadoste.categoria.models import Tipo, Cliente, Fornecedor

@admin.register(Tipo)
class Tipoadmin(admin.ModelAdmin):
   list_display = ['nome', 'descricao',]
   search_fields = ('nome', 'descricao',)

@admin.register(Cliente)
class Clienteadmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao',]
    search_fields = ('nome', 'descricao',)
    
@admin.register(Fornecedor)
class Fornecedoradmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao',]
    search_fields = ('nome', 'descricao',)
