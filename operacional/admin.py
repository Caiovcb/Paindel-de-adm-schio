from django.contrib import admin
from operacional.models import Login, RedeWifi, ManutencaoClienteFinal

@admin.register(Login)
class Loginadmin(admin.ModelAdmin):
    list_display = ['referencia', 'nome', 'nr_contato', 'email']
    search_fields = ('referencia', 'nome', 'nr_contato', 'email')

@admin.register(RedeWifi)
class RedeWifiadmin(admin.ModelAdmin):
    list_display = ['referencia', 'nome', 'nr_contato', 'email']
    search_fields = ('referencia', 'nome', 'nr_contato', 'email')

@admin.register(ManutencaoClienteFinal)
class ManutencaoClienteFinaladmin(admin.ModelAdmin):
    list_display = ['referencia', 'nome', 'nr_contato', 'email']
    search_fields = ('referencia', 'nome', 'nr_contato', 'email')