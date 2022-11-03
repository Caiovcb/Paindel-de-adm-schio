from django.db import models


class ClientesTe(models.Model):
    clientef = models.CharField(
        max_length=60, verbose_name='Cliente', null=True)
    cnpj = models.CharField(max_length=14, verbose_name='CPF/CNPJ',
        null=True, blank=True)
    nome = models.CharField(max_length=60, verbose_name='Nome', null=False)
    nr_contato = models.CharField(
        max_length=14,null=True, blank=False, verbose_name='Telefone')
    email = models.EmailField(max_length=70,verbose_name='Email', null=False)
    validacao_contrato = models.CharField(
        max_length=14,null=True, blank=True, verbose_name='Validação de contrato')
    validade_certificacao = models.DateField(
        null=True, blank=True, verbose_name='Validade de certificação')
    descricao = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.clientef

    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')
        ordering = ["clientef"]

