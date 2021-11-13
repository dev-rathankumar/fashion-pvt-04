# Generated by Django 3.1.4 on 2021-11-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0035_auto_20210905_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='storelocation',
            name='address_line_1_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='address_line_1_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='address_line_1_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='address_line_2_ar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='address_line_2_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='address_line_2_fr',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='city_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='city_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='city_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='store_name_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='store_name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='storelocation',
            name='store_name_fr',
            field=models.CharField(max_length=50, null=True),
        ),
    ]