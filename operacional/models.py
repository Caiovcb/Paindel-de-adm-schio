from django.db import models
from Clientes.models import ClientesTe



class Login(models.Model):
    referencia = models.ForeignKey(ClientesTe,
        on_delete=models.DO_NOTHING, verbose_name='Cliente')
    nome = models.CharField(
        max_length=60,verbose_name= 'Nome',null=True, blank=True)
    nr_contato = models.CharField(
        max_length=60,verbose_name= 'Telefone para Contato',null=True, blank=True)
    email = models.CharField(
        max_length=60,verbose_name= 'Email para Contato',null=True, blank=True)
    login = models.CharField(
        max_length=60,verbose_name= 'Login',null=True, blank=True)
    senha = models.CharField(
        max_length=60,verbose_name= 'Senha',null=True, blank=True)
    descricao = models.TextField(
        null=True, blank=True)


    class Meta:
        verbose_name = ('Login')
        verbose_name_plural = ('Login')
        ordering = ["referencia"]

class RedeWifi(models.Model):
    referencia = models.ForeignKey(ClientesTe,
        on_delete=models.DO_NOTHING, verbose_name='Cliente')
    nome = models.CharField(
        max_length=60,verbose_name= 'Nome',null=True, blank=True)
    nr_contato = models.CharField(
        max_length=60,verbose_name= 'telefone para Contato',null=True, blank=True)
    email = models.CharField(
        max_length=60,verbose_name= 'Email para Contato',null=True, blank=True)
    nome_rede = models.CharField(
        max_length=60,verbose_name= 'Rede',null=True, blank=True)
    senha = models.CharField(
        max_length=60,verbose_name= 'Senha',null=True, blank=True)
    descricao = models.TextField(
        null=True, blank=True)


    class Meta:
        verbose_name = ('Rede-Wifi')
        verbose_name_plural = ('Rede-Wifi')
        ordering = ["referencia"]

class ManutencaoClienteFinal(models.Model):
    referencia = models.ForeignKey(ClientesTe,
        on_delete=models.DO_NOTHING, verbose_name='Cliente')
    nome = models.CharField(
        max_length=60,verbose_name= 'Nome',null=True, blank=True)
    nr_contato = models.CharField(
        max_length=60,verbose_name= 'telefone para Contato',null=True, blank=True)
    email = models.CharField(
        max_length=60,verbose_name= 'Email para Contato',null=True, blank=True)
    descricao = models.TextField(
        null=True, blank=True)


    class Meta:
        verbose_name = ('Manutenção Cliente Final')
        verbose_name_plural = ('Manutenção Cliente Final')
        ordering = ["referencia"]