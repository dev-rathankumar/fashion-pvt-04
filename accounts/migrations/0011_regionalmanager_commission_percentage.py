# Generated by Django 3.1.4 on 2021-04-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210226_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionalmanager',
            name='commission_percentage',
            field=models.FloatField(default=0),
        ),
    ]
