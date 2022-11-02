from django.db import models


class ClientesTe(models.Model):
    nome = models.CharField(max_length=60, verbose_name='Nome')
    cnpj = models.CharField(max_length=14, verbose_name='CPF/CNPJ')
    email = models.EmailField(max_length=70,verbose_name='Email')
    tel_fixo = models.CharField(max_length=14, verbose_name='Telefone',
    null=True, blank=True)
    tel_celular = models.CharField(max_length=14, verbose_name='Celular',
    null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')
        ordering = ["nome"]

    
    
    