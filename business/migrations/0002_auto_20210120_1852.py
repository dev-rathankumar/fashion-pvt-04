# Generated by Django 3.1.4 on 2021-01-20 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testrathan',
            name='business_test',
        ),
        migrations.DeleteModel(
            name='SiteSetting',
        ),
        migrations.DeleteModel(
            name='TestRathan',
        ),
    ]
