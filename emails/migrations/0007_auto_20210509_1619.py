# Generated by Django 3.1.4 on 2021-05-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0006_auto_20210508_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='to_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
