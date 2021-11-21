# Generated by Django 3.1.4 on 2021-11-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_auto_20211011_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='first_name_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='first_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='first_name_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='inq_message_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='inq_message_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='inq_message_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='last_name_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='last_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='last_name_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='contact_message_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='contact_message_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='contact_message_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='name_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='name_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='subject_ar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='subject_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sitecontact',
            name='subject_fr',
            field=models.CharField(max_length=50, null=True),
        ),
    ]