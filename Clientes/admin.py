from django.contrib import admin
from .models import ClientesTe


admin.site.register(ClientesTe)
class Clientesadmin(admin.ModelAdmin):
    list_display = ['nome','cnpj', 'email',]
    
