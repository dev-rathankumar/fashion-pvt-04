# Generated by Django 3.1.4 on 2021-10-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0055_auto_20211018_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storefeature',
            name='sub_title',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='storefeature',
            name='title',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
