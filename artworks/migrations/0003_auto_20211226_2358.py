# Generated by Django 3.1.7 on 2021-12-26 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0002_auto_20211226_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voucher',
            old_name='editionNumber',
            new_name='edition_number',
        ),
        migrations.RenameField(
            model_name='voucher',
            old_name='priceDollar',
            new_name='price_dollar',
        ),
        migrations.RenameField(
            model_name='voucher',
            old_name='priceWei',
            new_name='price_wei',
        ),
    ]