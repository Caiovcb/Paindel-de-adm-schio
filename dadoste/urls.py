from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dadoste.paginas.urls')),
    path('', include('dadoste.usuarios.urls')),
    path('api-auth/', include('rest_framework.urls')),
]