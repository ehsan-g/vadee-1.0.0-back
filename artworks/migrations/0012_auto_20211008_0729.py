# Generated by Django 3.1.7 on 2021-10-08 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0011_auto_20211008_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artworks.artist'),
        ),
    ]