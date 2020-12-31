# Generated by Django 3.1.4 on 2020-12-31 20:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True)),
                ('product_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('inq_message', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.business')),
            ],
        ),
    ]
