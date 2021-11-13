# Generated by Django 3.1.4 on 2021-10-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20210930_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='variants',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]