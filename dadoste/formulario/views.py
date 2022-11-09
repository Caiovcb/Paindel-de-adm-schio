from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Formularios
from django.urls import reverse_lazy

########## CREATE ###########

class FormularioCreate(CreateView):
    model = Formularios
    fields=[
        'tipo',
        'cliente',
        'fornecedor',
        'cnpj',
        'nome',
        'nr_contato',
        'email',
        'validacao_contrato',
        'validade_certificacao',
        'descricao',        
    ]
    template_name = 'formulario/form.html'
    success_url = reverse_lazy('index')

########## UPDATE ###########

class FormularioUpdate(UpdateView):
    model = Formularios
    fields=[
        'tipo',
        'cliente',
        'fornecedor',
        'cnpj',
        'nome',
        'nr_contato',
        'email',
        'validacao_contrato',
        'validade_certificacao',
        'descricao',        
    ]
    template_name = 'formulario/form.html'
    success_url = reverse_lazy('index')

########## DELETE ###########

class FormularioDelete(DeleteView):
    model = Formularios
    template_name = 'formulario/form-excluir.html'
    success_url = reverse_lazy('index')


########## LIST ###########

class FormularioLista(ListView):
    model = Formularios
    template_name = 'formulario/listas/formulario.html'
