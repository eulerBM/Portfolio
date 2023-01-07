# Generated by Django 4.1.5 on 2023-01-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='descricao',
            field=models.TextField(max_length=300, null=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='nome',
            field=models.CharField(max_length=20, null=True, verbose_name='Nome do autor'),
        ),
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=30, null=True, verbose_name='Titulo da postagem'),
        ),
    ]