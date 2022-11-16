
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from rest_framework import status
from dadoste.formulario.models import Formularios
from dadoste.formulario.serializers import FormularioSerializers
from rest_framework.exceptions import NotFound

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
    success_url = reverse_lazy('listar')

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
    template_name = 'formulario/editarform.html'
    success_url = reverse_lazy('listar')

########## DELETE ###########

class FormularioDelete(DeleteView):
    model = Formularios
    template_name = 'formulario/form-excluir.html'
    success_url = reverse_lazy('listar')


########## LIST ###########

class FormularioLista(ListView):
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


