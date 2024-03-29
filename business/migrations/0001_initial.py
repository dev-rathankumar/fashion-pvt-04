# Generated by Django 3.1.4 on 2020-12-28 10:17

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRathan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=255)),
                ('business_test', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.business')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=255)),
                ('site_logo', models.ImageField(blank=True, max_length=500, upload_to='logos')),
                ('copyright', ckeditor.fields.RichTextField(blank=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.business')),
            ],
        ),
    ]
