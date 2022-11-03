from django.contrib import admin
from .models import ClientesTe


@admin.register(ClientesTe)
class Clientesadmin(admin.ModelAdmin):
    list_display = ['clientef','cnpj', 'email',]
    search_fields = ('clientef','cnpj','email',)
