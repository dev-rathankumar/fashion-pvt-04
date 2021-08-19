# Generated by Django 3.1.4 on 2021-08-18 08:34

import ckeditor.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0019_dashboardimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('featured_image', models.ImageField(upload_to='portfolio/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('live_preview_button', models.BooleanField(default=False)),
                ('button_name', models.CharField(blank=True, max_length=20, null=True)),
                ('button_link', models.CharField(blank=True, max_length=500, null=True)),
                ('button_bg_color', colorfield.fields.ColorField(blank=True, default='#000000', max_length=18, null=True)),
                ('button_text_color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', max_length=18, null=True)),
                ('button_alignment', models.CharField(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], default='center', max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.business')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=100)),
                ('sub_heading', models.TextField(blank=True, max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.business')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=5000, upload_to='portfolio/%Y/%m/%d')),
                ('portfolio', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio')),
            ],
            options={
                'verbose_name': 'portfoliogallery',
                'verbose_name_plural': 'portfolio gallery',
            },
        ),
    ]
