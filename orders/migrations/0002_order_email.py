# Generated by Django 3.1.4 on 2021-02-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='admin', max_length=50),
        ),
    ]
