# Generated by Django 3.1.7 on 2021-12-26 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0003_auto_20211226_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='in_stock',
        ),
    ]
