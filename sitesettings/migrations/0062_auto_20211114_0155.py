# Generated by Django 3.1.4 on 2021-11-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0061_auto_20211114_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='footer_text_ar',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='footer_text_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='footer_text_fr',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='site_title_ar',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='site_title_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='site_title_fr',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
