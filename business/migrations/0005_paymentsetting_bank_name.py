# Generated by Django 3.1.4 on 2021-02-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_paymentsetting_bank_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsetting',
            name='bank_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
