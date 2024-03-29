# Generated by Django 3.1.4 on 2021-01-01 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20210101_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitecontact',
            old_name='is_sent',
            new_name='is_otp_sent',
        ),
        migrations.RenameField(
            model_name='sitecontact',
            old_name='is_verified',
            new_name='is_otp_verified',
        ),
        migrations.RenameField(
            model_name='sitecontact',
            old_name='resend_counter',
            new_name='otp_resend_counter',
        ),
    ]
