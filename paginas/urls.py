from django.urls import path
from .views import PaginaLogin

urlpatterns = [
    #path ('Endereço/', MinhaView.as_view(), nome='nome_da_url'),
    path('', PaginaLogin.as_view(), name='Login'),
]

