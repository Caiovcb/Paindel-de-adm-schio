# Generated by Django 4.1.3 on 2022-11-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteste',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]