# Generated by Django 3.1.4 on 2021-11-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210503_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_ar',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_fr',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ar',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_fr',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
