from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsusarioCreate

urlpatterns = [
    #path ('Endereço/', MinhaView.as_view(), nome='nome_da_url'),
    path('', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar', UsusarioCreate.as_view(), name='registrar'),
]   