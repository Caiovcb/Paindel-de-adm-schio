# Generated by Django 4.1.3 on 2022-11-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0005_alter_clienteste_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteste',
            name='nr_contato',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Telefone'),
        ),
        migrations.AddField(
            model_name='clienteste',
            name='validacao_contrato',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Validação de contrato'),
        ),
        migrations.AddField(
            model_name='clienteste',
            name='validade_certificacao',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Validade de certificação'),
        ),
        migrations.AlterField(
            model_name='clienteste',
            name='clientef',
            field=models.CharField(max_length=60, null=True, verbose_name='Cliente'),
        ),
    ]
