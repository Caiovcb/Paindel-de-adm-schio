from django.urls import path
from dadoste.formulario.views import FormularioCreate, FormularioUpdate, FormularioDelete
from dadoste.categoria.views import ClienteCreate, ClienteDelete, ClienteLista, ClienteUpdate, FornecedorCreate, FornecedorDelete, FornecedorLista, FornecedorUpdate, TipoCreate, TipoDelete, TipoLista, TipoUpdate
from .views import Index, Sobre
from dadoste.formulario.views import FormularioLista
urlpatterns = [
    #path ('Endereço/', MinhaView.as_view(), nome='nome_da_url'),
    path('index', Index.as_view(), name='index'),
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
    #DELETE
    path('formulario/excluir/<int:pk>/', FormularioDelete.as_view(), name='excluir' ),
    path('tipo/excluir/<int:pk>/', TipoDelete.as_view(), name='excluir-tipo' ),
    path('cliente/excluir/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente' ),
    path('fornecedor/excluir/<int:pk>/', FornecedorDelete.as_view(), name='excluir-fornecedor' ),
    #LISTA
    path('', FormularioLista.as_view(), name='listar' ),
    path('tipo/listar', TipoLista.as_view(), name='listar-tipo' ),
    path('cliente/listar', ClienteLista.as_view(), name='listar-cliente' ),
    path('fornecedor/listar', FornecedorLista.as_view(), name='listar-fornecedor' ),

]

