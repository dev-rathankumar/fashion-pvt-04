# Generated by Django 3.1.4 on 2021-11-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20211011_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='salespopup',
            name='location_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='salespopup',
            name='location_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='salespopup',
            name='location_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='salespopup',
            name='name_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='salespopup',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='salespopup',
            name='name_fr',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
