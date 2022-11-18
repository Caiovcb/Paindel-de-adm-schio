
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from rest_framework.decorators import api_view
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from dadoste.formulario.models import Formularios
from dadoste.formulario.serializers import FormularioSerializers


########## CREATE ###########

class FormularioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Formularios
    fields=[
        'tipo',
        'cliente',
        'fornecedor',
        'nome',
        'cnpj',
        'nr_contato',
        'email',
        'validacao_contrato',
        'validade_certificacao',
        'descricao',        
    ]
    template_name = 'formulario/form.html'
    success_url = reverse_lazy('listar')

########## UPDATE ###########

class FormularioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Formularios
    fields=[
        'tipo',
        'cliente',
        'fornecedor',
        'nome',
        'cnpj',
        'nr_contato',
        'email',
        'validacao_contrato',
        'validade_certificacao',
        'descricao',        
    ]
    template_name = 'formulario/editarform.html'
    success_url = reverse_lazy('listar')

class FormularioVer(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Formularios
    fields=[
        'tipo',
        'cliente',
        'fornecedor',
        'nome',
        'cnpj',
        'nr_contato',
        'email',
        'validacao_contrato',
        'validade_certificacao',
        'descricao',        
    ]
    template_name = 'formulario/editarform.html'
    success_url = reverse_lazy('listar')
    

########## DELETE ###########

class FormularioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Formularios
    template_name = 'formulario/form-excluir.html'
    success_url = reverse_lazy('listar')


########## LIST ###########

class FormularioLista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Formularios
    template_name = 'formulario/listas/formulario.html'

'''   def get_queryset(self):

        txt_tipo = self.request.GET.get('tipo')

        if txt_tipo:           
            formulario =formulario.objects.filter(nome__icontains= txt_tipo)
        else:
            formulario = formulario.objects.all()   
        return formulario'''



class FormularioListaCriacao(generics.ListCreateAPIView):
    queryset = Formularios.objects.all()
    serializer_class = FormularioSerializers
 
class FormularioAteracaoDetalheDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formularios.objects.all()
    serializer_class = FormularioSerializers


