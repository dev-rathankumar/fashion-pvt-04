# Generated by Django 3.1.4 on 2021-09-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20210906_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salespopup',
            name='interval',
            field=models.CharField(choices=[('Seconds', 'Seconds'), ('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days')], default='Seconds', max_length=50),
        ),
    ]
