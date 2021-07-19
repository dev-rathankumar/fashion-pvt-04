# Generated by Django 3.1.4 on 2021-07-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0034_paypalconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='hard_code_branding',
            field=models.CharField(blank=True, default='Altocan', max_length=100),
        ),
        migrations.AddField(
            model_name='footer',
            name='hard_code_footer',
            field=models.CharField(blank=True, default='Provided by', max_length=100),
        ),
        migrations.AddField(
            model_name='footer',
            name='hard_code_url',
            field=models.URLField(blank=True, default='https://www.altocan.com/'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='footer_text',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
