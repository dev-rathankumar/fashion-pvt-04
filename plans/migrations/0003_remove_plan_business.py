# Generated by Django 3.1.4 on 2021-04-16 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20210417_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='business',
        ),
    ]
