from django.urls import path
from .views import IndexView

urlpatterns = [
    #path ('Endereço/', MinhaView.as_view(), nome='nome_da_url'),
    path('', IndexView.as_view(), name='Index'),
]

