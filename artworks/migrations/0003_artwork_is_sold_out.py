# Generated by Django 3.1.7 on 2021-12-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0002_auto_20211229_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='is_sold_out',
            field=models.BooleanField(default=True),
        ),
    ]
