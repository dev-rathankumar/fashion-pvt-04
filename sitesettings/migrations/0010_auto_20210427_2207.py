# Generated by Django 3.1.4 on 2021-04-27 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0009_auto_20210427_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='button_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
