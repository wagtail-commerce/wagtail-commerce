# Generated by Django 2.2.5 on 2020-09-12 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_shipping', '0005_auto_20200912_0218'),
        ('wagtailcommerce_orders', '0024_auto_20190910_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='language_code',
            field=models.CharField(default='', max_length=40, verbose_name='language code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='wagtailcommerce_shipping.ShippingMethod', verbose_name='shipping method'),
        ),
    ]