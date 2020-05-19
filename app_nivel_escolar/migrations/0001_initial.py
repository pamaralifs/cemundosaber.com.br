# Generated by Django 3.0.6 on 2020-05-08 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NivelEscolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Nível Escolar',
                'verbose_name_plural': 'Níveis Escolares',
            },
        ),
    ]
