# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-30 01:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_carts', '0002_auto_20180129_0244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartline',
            options={'ordering': ('created',), 'verbose_name': 'cart line', 'verbose_name_plural': 'cart lines'},
        ),
    ]
