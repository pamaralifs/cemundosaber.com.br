# Generated by Django 3.0.6 on 2020-05-09 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0002_auto_20200508_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acesso',
            name='data_hora_acesso',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='DATA HORA ACESSO'),
        ),
    ]
