# Generated by Django 3.1.7 on 2021-12-30 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0013_auto_20211230_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thetoken',
            name='token_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
