# Generated by Django 3.1.4 on 2021-04-27 18:18

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0011_auto_20210427_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='parallaxbackground',
            name='button_link',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='parallaxbackground',
            name='button_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AlterField(
            model_name='parallaxbackground',
            name='content_align',
            field=models.CharField(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], default='center', max_length=10),
        ),
    ]