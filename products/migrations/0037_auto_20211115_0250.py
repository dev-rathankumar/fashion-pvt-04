# Generated by Django 3.1.4 on 2021-11-14 21:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_auto_20211115_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_ar',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_fr',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='full_specification_ar',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='full_specification_en',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='full_specification_fr',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_ar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_fr',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
