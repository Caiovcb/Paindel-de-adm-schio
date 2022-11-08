from django.urls import path
from .views import PaginaLogin, Paginasobre

urlpatterns = [
    #path ('Endereço/', MinhaView.as_view(), nome='nome_da_url'),
    path('', PaginaLogin.as_view(), name='Login'),
    path('sobre', Paginasobre.as_view(), name='Sobre'),
]

