# Generated by Django 2.2.5 on 2020-09-12 05:18

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcommerce_shipping', '0004_auto_20190910_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='shipping_label',
            field=models.FileField(blank=True, upload_to='shipping_labels/', verbose_name='shipping label'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='tracking_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='tracking link'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='display_title',
            field=models.CharField(blank=True, help_text='Displayed on frontends instead of the title field', max_length=200, verbose_name='display title'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enabled'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='enabled_for_administrators',
            field=models.BooleanField(default=False, help_text="It will be available for admin users even if it's not enabled for the general public", verbose_name='enabled for administrators'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='free_shipping_above_amount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='If the cart total is above this amount, shipping will be free', max_digits=12, null=True, verbose_name='free shipping above amount'),
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='sort_order',
            field=models.PositiveIntegerField(default=0, help_text='Shipping methods with a higher sort order will appear closer to the end on listings', verbose_name='sort order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingmethod',
            name='title',
            field=models.CharField(default='Shipping Method Title', max_length=200, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ShippingRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country')),
                ('postal_codes', models.TextField(blank=True, help_text='Enter postal codes separated by commas, e.g. "3547,7894,45 545,as 51 d"', verbose_name='postal codes')),
                ('shipping_method', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_regions', to='wagtailcommerce_shipping.ShippingMethod')),
            ],
            options={
                'verbose_name': 'shipping region',
                'verbose_name_plural': 'shipping regions',
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
