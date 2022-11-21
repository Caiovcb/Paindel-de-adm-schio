#from Clientes.models import ClientesTe
from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=60, unique=True, verbose_name='Tipo de Informação')
    descricao = models.TextField(
        null=True, blank=True)

    def __str__(self) -> str:
        return str(self.nome)

    class Meta:
        verbose_name = ('Tipo')
        verbose_name_plural = ('Tipos')
        ordering = ["nome"]

class Cliente(models.Model):
    nome = models.CharField(max_length=60, unique=True, verbose_name='Cliente')
    descricao = models.TextField(
        null=True, blank=True)

    def __str__(self) -> str:
        return str(self.nome)

    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')
        ordering = ["nome"]

class Fornecedor(models.Model):
    nome = models.CharField(max_length=60, unique=True, verbose_name='Fornecedor')
    descricao = models.TextField(
        null=True, blank=True)

    def __str__(self) -> str:
        return str(self.nome)

    class Meta:
        verbose_name = ('Fornecedor')
        verbose_name_plural = ('Fornecedores')
        ordering = ["nome"]
