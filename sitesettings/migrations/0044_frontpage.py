# Generated by Django 3.1.4 on 2021-09-26 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_dashboardimage'),
        ('sitesettings', '0043_auto_20210925_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_page_name', models.CharField(max_length=50)),
                ('preview_image', models.ImageField(blank=True, upload_to='frontpages')),
                ('preview_link', models.URLField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.business')),
            ],
        ),
    ]