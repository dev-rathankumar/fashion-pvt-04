# Generated by Django 3.1.4 on 2021-08-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0037_auto_20210810_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
