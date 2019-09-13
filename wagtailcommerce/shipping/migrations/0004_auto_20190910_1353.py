# Generated by Django 2.2.5 on 2019-09-10 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_shipping', '0003_shipment_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='shipping_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipments', to='wagtailcommerce_shipping.ShippingMethod'),
        ),
        migrations.AlterField(
            model_name='shippingmethod',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shipping_methods', to='wagtailcommerce_stores.Store'),
        ),
    ]