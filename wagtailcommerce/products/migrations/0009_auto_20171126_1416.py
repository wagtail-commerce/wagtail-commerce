# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_products', '0008_auto_20171126_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='product',
            name='single_price',
            field=models.BooleanField(default=True, help_text='same price for all variants', verbose_name='single price'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='price'),
        ),
    ]
