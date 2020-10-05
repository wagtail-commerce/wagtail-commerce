# Generated by Django 2.2.5 on 2020-10-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_orders', '0026_auto_20200914_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='item_percentage_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='percentage discount'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='item_unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='unit price'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='item_unit_price_with_promotions_discount',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='unit price with promotions discount'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='item_unit_promotions_discount',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='per unit discount unit based on promotions'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='item_unit_regular_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='unit regular price'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='item_unit_sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='unit sale price'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='line_total',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='subtotal'),
        ),
    ]
