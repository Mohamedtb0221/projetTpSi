# Generated by Django 4.1.2 on 2023-01-28 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_deces_numn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deces',
            name='date_naiss',
        ),
        migrations.RemoveField(
            model_name='deces',
            name='lieu_naiss',
        ),
        migrations.RemoveField(
            model_name='deces',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='deces',
            name='prenoms',
        ),
        migrations.RemoveField(
            model_name='deces',
            name='sexe',
        ),
    ]
