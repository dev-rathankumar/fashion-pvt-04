# Generated by Django 3.1.4 on 2021-11-13 19:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0058_auto_20211114_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerimage',
            name='button_name_ar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='button_name_en',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='button_name_fr',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='sub_title_ar',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='sub_title_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='sub_title_fr',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='title_ar',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='title_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='title_fr',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]