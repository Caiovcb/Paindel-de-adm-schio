from django.db import models
from categoria.models import Tipo, Cliente, Fornecedor


class Formularios(models.Model):
    tipo = models.ForeignKey(
        Tipo, on_delete=models.PROTECT)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, null=True, blank=True)
    cnpj = models.CharField(
        max_length=14, verbose_name='CPF/CNPJ',
        null=True, blank=True)
    nome = models.CharField(
        max_length=60, verbose_name='Nome', null=True, blank=True)
    nr_contato = models.CharField(
        max_length=14,null=True, blank=True, verbose_name='Telefone', )
    email = models.EmailField(
        max_length=70,verbose_name='Email', null=True , blank=True)
    validacao_contrato = models.CharField(
        max_length=14,null=True,
        blank=True, verbose_name='Validação de contrato')
    validade_certificacao = models.DateField(
        null=True, blank=True, verbose_name='Validade de certificação')
    descricao = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return str(self.tipo)

    class Meta:
        verbose_name = ('Formulario Geral')
        verbose_name_plural = ('Formulario Geral')
        ordering = ['tipo']
