# Generated by Django 4.1.1 on 2022-10-14 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='link_1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='link_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='link_3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='link_4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='descricao',
            field=models.TextField(),
        ),
    ]
