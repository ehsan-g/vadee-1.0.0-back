# Generated by Django 3.1.7 on 2021-09-26 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0005_remove_myuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]