# Generated by Django 3.1.4 on 2021-11-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20211115_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_body_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_body_fr',
            field=models.TextField(null=True),
        ),
    ]
