# Generated by Django 3.0.8 on 2020-10-09 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_transacoes_saldo_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transacoes',
            name='saldo_data',
        ),
    ]
