# Generated by Django 3.1.4 on 2021-08-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
