# Generated by Django 4.1.3 on 2022-11-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0003_alter_formularios_nr_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularios',
            name='nr_contato',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Telefone'),
        ),
    ]
