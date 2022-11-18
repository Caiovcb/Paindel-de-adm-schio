from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tipo, Cliente, Fornecedor
from django.urls import reverse_lazy

class TipoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tipo
    fields=[
        'nome',     
    ]
    template_name = 'categoria/tipoform.html'
    success_url = reverse_lazy('listar-tipo')

class ClienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields=[
        'nome',     
    ]
    template_name = 'categoria/clienteform.html'
    success_url = reverse_lazy('listar-cliente')

class FornecedorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields=[
        'nome',     
    ]
    template_name = 'categoria/fornecedorform.html'
    success_url = reverse_lazy('listar-fornecedor')

#UPDATE#

class TipoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tipo
    fields=[
        'nome',     
    ]
    template_name = 'categoria/tipoformupdate.html'
    success_url = reverse_lazy('listar-tipo')

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields=[
        'nome',     
    ]
    template_name = 'categoria/clienteformupdate.html'
    success_url = reverse_lazy('listar-cliente')

class FornecedorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields=[
        'nome',     
    ]
    template_name = 'categoria/fornecedorformupdate.html'
    success_url = reverse_lazy('listar-fornecedor')

#DELETE#
    
class TipoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tipo
    template_name = 'categoria/tipoformdelete.html'
    success_url = reverse_lazy('listar-tipo')

class ClienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'categoria/clienteformdelete.html'
    success_url = reverse_lazy('listar-cliete')

class FornecedorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'categoria/fornecedorformdelete.html'
    success_url = reverse_lazy('listar-fornecedor')

#### LISTA   ##########

class TipoLista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tipo
    template_name = 'categoria/listas/listatipo.html'

class ClienteLista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'categoria/listas/listaclientes.html'

class FornecedorLista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'categoria/listas/listafornecedor.html'
