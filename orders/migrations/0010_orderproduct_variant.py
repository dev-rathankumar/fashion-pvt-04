# Generated by Django 3.1.4 on 2021-02-20 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_full_specification'),
        ('orders', '0009_auto_20210220_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='variant',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='products.variants'),
        ),
    ]
