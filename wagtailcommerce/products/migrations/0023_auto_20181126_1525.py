# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_products', '0022_auto_20180711_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='search_description',
            field=models.TextField(blank=True, verbose_name='search description'),
        ),
        migrations.AddField(
            model_name='product',
            name='seo_title',
            field=models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, verbose_name='page title'),
        ),
    ]