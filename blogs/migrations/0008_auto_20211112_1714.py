# Generated by Django 3.1.4 on 2021-11-12 11:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20211112_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_body_ar',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_body_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_body_fr',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
