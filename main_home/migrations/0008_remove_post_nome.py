# Generated by Django 4.1.5 on 2023-01-07 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_home', '0007_remove_post_link_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='nome',
        ),
    ]
