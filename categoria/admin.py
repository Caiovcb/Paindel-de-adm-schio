from django.contrib import admin
from operacional.models import Login, RedeWifi, ManutencaoClienteFinal

@admin.register(Login)
class Loginadmin(admin.ModelAdmin):
   list_display = ['referencia',]
   search_fields = ('referencia',)

@admin.register(RedeWifi)
class RedeWifiadmin(admin.ModelAdmin):
    list_display = ['referencia',]
    search_fields = ('referencia',)
    
@admin.register(ManutencaoClienteFinal)
class ManutencaoClienteFinaladmin(admin.ModelAdmin):
    list_display = ['referencia',]
    search_fields = ('referencia',)
