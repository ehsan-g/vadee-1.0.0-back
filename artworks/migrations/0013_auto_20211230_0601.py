# Generated by Django 3.1.7 on 2021-12-30 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0012_auto_20211230_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thetoken',
            name='artwork',
        ),
        migrations.AddField(
            model_name='thetoken',
            name='artwork',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='token_artwork', to='artworks.artwork'),
        ),
    ]
