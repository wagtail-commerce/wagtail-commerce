# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcommerce_products', '0005_auto_20170918_1729'),
        ('wagtailcommerce_stores', '0001_initial'),
        ('wagtailcommerce_addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='product sub total')),
                ('product_discount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='product discount')),
                ('product_tax', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='product tax')),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='shipping cost')),
                ('shipping_cost_discount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='shipping cost discount')),
                ('shipping_cost_tax', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='shipping cost tax')),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='order total')),
                ('total_inc_tax', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='order total (inc. tax)')),
                ('voucher_type', models.CharField(blank=True, choices=[('category', 'Products in categories'), ('products', 'Specific products'), ('shipping', 'Shipping cost')], max_length=20, verbose_name='voucher type')),
                ('voucher_mode', models.CharField(blank=True, choices=[('fixed', 'Fixed amount'), ('percentage', 'Percentage')], max_length=20, verbose_name='voucher mode')),
                ('voucher_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='voucher amount')),
                ('voucher_code', models.CharField(blank=True, max_length=40, verbose_name='voucher code')),
                ('date_placed', models.DateTimeField(db_index=True)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_by_billing_address', to='wagtailcommerce_addresses.Address')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_by_shipping_address', to='wagtailcommerce_addresses.Address')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wagtailcommerce_stores.Store')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=128, verbose_name='SKU')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
                ('line_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='line price')),
                ('voucher_type', models.CharField(blank=True, choices=[('category', 'Products in categories'), ('products', 'Specific products'), ('shipping', 'Shipping cost')], max_length=20, verbose_name='discount type')),
                ('voucher_mode', models.CharField(blank=True, choices=[('fixed', 'Fixed amount'), ('percentage', 'Percentage')], max_length=20, verbose_name='discount mode')),
                ('voucher_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='discount amount')),
                ('voucher_voucher_code', models.CharField(blank=True, max_length=40, verbose_name='code')),
                ('product_name', models.CharField(max_length=255, verbose_name='product name')),
                ('product_variant_description', models.CharField(max_length=255, verbose_name='product variant description')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='wagtailcommerce_orders.Order')),
                ('product_variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lines', to='wagtailcommerce_products.ProductVariant')),
            ],
            options={
                'verbose_name': 'order line',
                'verbose_name_plural': 'order lines',
            },
        ),
    ]
