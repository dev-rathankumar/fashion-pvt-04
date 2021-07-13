# Generated by Django 3.1.4 on 2021-07-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_auto_20210712_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('On Hold', 'On Hold'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=15),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('On Hold', 'On Hold'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]
