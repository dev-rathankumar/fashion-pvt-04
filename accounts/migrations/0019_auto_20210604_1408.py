# Generated by Django 3.1.4 on 2021-06-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20210508_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='account_expiry_date',
            field=models.DateField(null=True),
        ),
    ]
