# Generated by Django 4.1.3 on 2022-11-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0011_delete_tipodainfo'),
        ('operacional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(blank=True, max_length=60, null=True, verbose_name='Login')),
                ('senha', models.CharField(blank=True, max_length=60, null=True, verbose_name='Senha')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Clientes.clienteste', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Login',
                'verbose_name_plural': 'Login',
                'ordering': ['referencia'],
            },
        ),
        migrations.DeleteModel(
            name='Operacional',
        ),
    ]
