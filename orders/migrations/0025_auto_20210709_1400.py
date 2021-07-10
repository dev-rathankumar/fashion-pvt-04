# Generated by Django 3.1.4 on 2021-07-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20210506_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('paypal', 'PayPal'), ('direct deposit', 'Direct Deposit')], default='paypal', max_length=100),
        ),
    ]