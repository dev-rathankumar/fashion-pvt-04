# Generated by Django 3.1.4 on 2021-06-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20210529_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
