# Generated by Django 3.1.4 on 2021-04-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20210416_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxsetting',
            name='tax_value',
            field=models.DecimalField(decimal_places=2, help_text="Data format: {'tax_type':{'tax_value':'tax_amount'}}", max_digits=4),
        ),
    ]
