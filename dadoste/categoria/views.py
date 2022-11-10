from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Tipo, Cliente, Fornecedor
from django.urls import reverse_lazy

class TipoCreate(CreateView):
    model = Tipo
    fields=[
        'nome',     
    ]
    template_name = 'categoria/tipoform.html'
    success_url = reverse_lazy('listar')

class ClienteCreate(CreateView):
    model = Cliente
    fields=[
        'nome',     
    ]
    template_name = 'categoria/clienteform.html'
    success_url = reverse_lazy('listar')

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields=[
        'nome',     
    ]
    template_name = 'categoria/fornecedorform.html'
    success_url = reverse_lazy('listar')

#UPDATE#

class TipoUpdate(UpdateView):
    model = Tipo
    fields=[
        'nome',     
    ]
    template_name = 'categoria/tipoform.html'
    success_url = reverse_lazy('listar')

class ClienteUpdate(UpdateView):
    model = Cliente
    fields=[
        'nome',     
    ]
    template_name = 'categoria/clienteform.html'
    success_url = reverse_lazy('listar')

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields=[
        'nome',     
    ]
    template_name = 'categoria/fornecedorform.html'
    success_url = reverse_lazy('listar')

#DELETE#
    