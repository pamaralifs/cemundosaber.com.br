# Generated by Django 3.0.6 on 2020-05-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_material', '0004_auto_20200510_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='tornar_visivel',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='S', max_length=1, verbose_name='Visível'),
        ),
    ]
