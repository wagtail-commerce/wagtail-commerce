# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-22 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_orders', '0003_auto_20180122_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_placed',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]