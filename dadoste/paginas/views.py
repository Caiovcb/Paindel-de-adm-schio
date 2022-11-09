from django.views.generic import TemplateView
 
class PaginaLogin(TemplateView):
    template_name = 'modelo.html'

class Sobre(TemplateView):
    template_name = 'sobre.html'

class Index(TemplateView):
    template_name = 'index.html'