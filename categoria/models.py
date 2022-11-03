from django.db import models
from Clientes.models import ClientesTe



class Login(models.Model):
    referencia = models.ForeignKey(ClientesTe,
        on_delete=models.DO_NOTHING, verbose_name='Tipo')
    descricao = models.TextField(
        null=True, blank=True)


    class Meta:
        verbose_name = ('Tipo')
        verbose_name_plural = ('Tipo')
        ordering = ["referencia"]

class RedeWifi(models.Model):
    referencia = models.ForeignKey(ClientesTe,
        on_delete=models.DO_NOTHING, verbose_name='Cliente')
    descricao = models.TextField(
        null=True, blank=True)


    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Cliente')
        ordering = ["referencia"]

class ManutencaoClienteFinal(models.Model):
    referencia = models.ForeignKey(ClientesTe,
        on_delete=models.DO_NOTHING, verbose_name='Cliente')
    descricao = models.TextField(
        null=True, blank=True)


    class Meta:
        verbose_name = ('Fornecedor')
        verbose_name_plural = ('Fornecedores')
        ordering = ["referencia"]
