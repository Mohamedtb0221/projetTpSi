# Generated by Django 4.1.2 on 2023-01-28 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_naissance_date_naiss_mere_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naissance',
            name='grand_mere_m',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gmereminfo', to='app1.naissance'),
        ),
        migrations.AlterField(
            model_name='naissance',
            name='grand_mere_p',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gmerepinfo', to='app1.naissance'),
        ),
        migrations.AlterField(
            model_name='naissance',
            name='grand_pere_m',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gpereminfo', to='app1.naissance'),
        ),
        migrations.AlterField(
            model_name='naissance',
            name='grand_pere_p',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gperepinfo', to='app1.naissance'),
        ),
        migrations.AlterField(
            model_name='naissance',
            name='merei',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mereinfo', to='app1.naissance'),
        ),
        migrations.AlterField(
            model_name='naissance',
            name='perei',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pereinfo', to='app1.naissance'),
        ),
    ]
