# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-20 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_products', '0022_auto_20180711_1526'),
        ('wagtailcommerce_promotions', '0008_auto_20180319_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='categories',
            field=models.ManyToManyField(blank=True, help_text='Only apply to products in selected categories', related_name='coupons', to='wagtailcommerce_products.Category'),
        ),
    ]
