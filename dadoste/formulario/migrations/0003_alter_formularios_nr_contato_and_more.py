# Generated by Django 4.1.3 on 2022-11-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_formularios_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularios',
            name='nr_contato',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='formularios',
            name='validacao_contrato',
            field=models.DateField(blank=True, null=True, verbose_name='Validação de contrato'),
        ),
    ]
