from django.db import models


class ClientesTe(models.Model):
    cliente = models.CharField(max_length=60, verbose_name='Cliente')
    nome = models.CharField(max_length=60, verbose_name='Nome')
    email = models.EmailField(max_length=70,verbose_name='Email')
    tel_contato = models.CharField(max_length=14, verbose_name='Telefone',)
    cnpj = models.CharField(max_length=14, verbose_name='CPF/CNPJ',
        null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    validacao_contrato = models.DateField()

    
    def __str__(self):
        return self.cliente

    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')
        ordering = ["cliente"]

    
    
    