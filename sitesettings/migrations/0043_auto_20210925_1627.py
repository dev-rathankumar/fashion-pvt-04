# Generated by Django 3.1.4 on 2021-09-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0042_auto_20210914_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='sub_title',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
