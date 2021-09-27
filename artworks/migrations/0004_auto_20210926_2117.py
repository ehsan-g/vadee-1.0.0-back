# Generated by Django 3.1.7 on 2021-09-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0003_auto_20210925_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='nick_name',
            new_name='city',
        ),
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='myuser',
            name='country',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='postal_code',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
