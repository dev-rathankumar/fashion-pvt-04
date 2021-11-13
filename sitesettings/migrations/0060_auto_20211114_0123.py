# Generated by Django 3.1.4 on 2021-11-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0059_auto_20211114_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='storefeature',
            name='sub_title_ar',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='storefeature',
            name='sub_title_en',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='storefeature',
            name='sub_title_fr',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='storefeature',
            name='title_ar',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='storefeature',
            name='title_en',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='storefeature',
            name='title_fr',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]