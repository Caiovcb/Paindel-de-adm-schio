from django.urls import path
from dadoste.formulario.views import FormularioCreate, FormularioUpdate, FormularioDelete
from .views import Index, Sobre
from dadoste.formulario.views import FormularioLista
urlpatterns = [
    #path ('Endereço/', MinhaView.as_view(), nome='nome_da_url'),
    path('', Index.as_view(), name='index'),
    path('sobre', Sobre.as_view(), name='Sobre'),
    path('formulario/cadastro', FormularioCreate.as_view(), name='cadastro'),

    path('formulario/update/<int:pk>/', FormularioUpdate.as_view(), name='update' ),

    path('formulario/excluir/<int:pk>/', FormularioDelete.as_view(), name='excluir' ),

    path('formulario/listar/', FormularioLista.as_view(), name='listar' ),

]

