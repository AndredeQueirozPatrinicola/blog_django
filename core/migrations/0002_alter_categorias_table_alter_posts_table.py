# Generated by Django 4.0.5 on 2022-07-18 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categorias',
            table='categoria',
        ),
        migrations.AlterModelTable(
            name='posts',
            table='post',
        ),
    ]
