from django.contrib import admin
from .models import ClientesTe


admin.site.register(ClientesTe)
class Clientesadmin(admin.ModelAdmin):
    ist_display=('nome','cnppj', 'email' )
    search_fields=('nome', 'cnpj', 'email')

