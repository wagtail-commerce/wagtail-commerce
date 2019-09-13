# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_orders', '0013_auto_20180129_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='line_price',
        ),
        migrations.AddField(
            model_name='orderline',
            name='item_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='item discount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderline',
            name='item_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='item price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderline',
            name='item_price_with_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='item price with discount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderline',
            name='line_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='total'),
            preserve_default=False,
        ),
    ]