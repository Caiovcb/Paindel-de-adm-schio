from django.contrib import admin
from .models import ClientesTe


@admin.register(ClientesTe)
class Clientesadmin(admin.ModelAdmin):
    list_display = ['nome','cnpj', 'email',]
    search_fields = ('nome','cnpj','email',)

