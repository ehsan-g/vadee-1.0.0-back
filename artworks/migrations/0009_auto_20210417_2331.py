# Generated by Django 3.1.7 on 2021-04-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0008_auto_20210417_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='title',
            field=models.CharField(blank=True, default='no title', max_length=200, null=True),
        ),
    ]
