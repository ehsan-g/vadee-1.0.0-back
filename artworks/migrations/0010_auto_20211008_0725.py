# Generated by Django 3.1.7 on 2021-10-08 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0009_auto_20211008_0719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artwork',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'artworks'},
        ),
    ]
