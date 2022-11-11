from django.urls import path
from dadoste.formulario.views import FormularioCreate, FormularioUpdate, FormularioDelete
from dadoste.categoria.views import ClienteCreate, ClienteUpdate, FornecedorCreate, FornecedorUpdate, TipoCreate, TipoUpdate
from .views import Index, Sobre
from dadoste.formulario.views import FormularioLista
urlpatterns = [
    #path ('Endereço/', MinhaView.as_view(), nome='nome_da_url'),
    path('xxx', Index.as_view(), name='index'),
    path('sobre', Sobre.as_view(), name='Sobre'),
    #CREATE
    path('formulario/cadastro', FormularioCreate.as_view(), name='cadastro'),
    path('tipo/cadastro', TipoCreate.as_view(), name='tipo-cadastro'),
    path('cliente/cadastro', ClienteCreate.as_view(), name='cliente-cadastro'),
    path('fornecedor/cadastro', FornecedorCreate.as_view(), name='fornecedor-cadastro'),
    #UPDATE
    path('formulario/update/<int:pk>/', FormularioUpdate.as_view(), name='update' ),
    path('tipo/update/<int:pk>/', TipoUpdate.as_view(), name='tipo-update' ),
    path('cliente/update/<int:pk>/', ClienteUpdate.as_view(), name='cliente-update' ),
    path('fornecedor/update/<int:pk>/', FornecedorUpdate.as_view(), name='fornecedor-update' ),

    path('formulario/excluir/<int:pk>/', FormularioDelete.as_view(), name='excluir' ),

    path('', FormularioLista.as_view(), name='listar' ),

]

