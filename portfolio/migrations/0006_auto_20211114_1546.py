# Generated by Django 3.1.4 on 2021-11-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20211114_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioheader',
            name='heading_ar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolioheader',
            name='heading_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolioheader',
            name='heading_fr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolioheader',
            name='sub_heading_ar',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfolioheader',
            name='sub_heading_en',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfolioheader',
            name='sub_heading_fr',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
