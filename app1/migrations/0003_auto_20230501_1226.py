# Generated by Django 2.2.13 on 2023-05-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20230430_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='Location',
        ),
        migrations.AddField(
            model_name='login',
            name='Latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='login',
            name='Longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
