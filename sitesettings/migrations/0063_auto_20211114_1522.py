# Generated by Django 3.1.4 on 2021-11-14 09:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0062_auto_20211114_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='address_line_1_ar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='address_line_1_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='address_line_1_fr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='address_line_2_ar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='address_line_2_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='address_line_2_fr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='city_ar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='city_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='city_fr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='content_ar',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='content_fr',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='heading_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='heading_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='heading_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='button_name_ar',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='button_name_en',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='button_name_fr',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='sub_title_ar',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='sub_title_en',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='sub_title_fr',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='title_ar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='title_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='servicepagecta',
            name='title_fr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='content_ar',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='content_fr',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='heading_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='heading_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='termsandcondition',
            name='heading_fr',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
