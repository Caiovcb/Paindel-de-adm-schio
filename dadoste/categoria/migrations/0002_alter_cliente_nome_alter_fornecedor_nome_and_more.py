# Generated by Django 4.1.3 on 2022-11-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=60, verbose_name='Cliente * '),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome',
            field=models.CharField(max_length=60, verbose_name='Fornecedor * '),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nome',
            field=models.CharField(max_length=60, verbose_name='Tipo de Informação * '),
        ),
    ]
