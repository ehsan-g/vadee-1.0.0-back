# Generated by Django 3.1.7 on 2021-12-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0010_remove_order_paid_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='fee_eth',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_eth',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True),
        ),
    ]
