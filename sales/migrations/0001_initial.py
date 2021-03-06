# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-11 08:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financial', '0001_initial'),
        ('products', '0001_initial'),
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'sales_cart_item',
                'verbose_name_plural': 'Cart Items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('refunded_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('exchange_rate', models.FloatField(default=1)),
                ('charge_amount', models.DecimalField(decimal_places=2, help_text='Order total amount in user prefered currency that has been charged.', max_digits=9)),
                ('order_status', models.CharField(choices=[('PE', 'Pending'), ('PR', 'Processing'), ('CO', 'Complete'), ('CA', 'Cancelled')], max_length=2)),
                ('payment_status', models.CharField(choices=[('PE', 'Pending'), ('AU', 'Authorized'), ('PA', 'Paid'), ('PR', 'Partially Refunded'), ('RE', 'Refunded'), ('VO', 'Void')], max_length=2)),
                ('po_number', models.CharField(blank=True, help_text='Purchase Order number', max_length=100, null=True)),
                ('shipping_status', models.CharField(choices=[('NR', 'Not Required'), ('PE', 'Pending'), ('PS', 'Partially Shipped'), ('SH', 'Shipped'), ('DE', 'Delivered')], max_length=2)),
                ('receipt_code', models.CharField(help_text='Random code generate for each order for secure access.', max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_orders', to='geo.Address')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial.Currency')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, help_text='Unit price of the product', max_digits=9)),
                ('quantity', models.IntegerField()),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=9)),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('tax_rate', models.FloatField(default=0.0)),
                ('tax_method', models.CharField(blank=True, choices=[('PE', 'Percentage'), ('FI', 'Fixed')], max_length=2, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'db_table': 'sales_order_item',
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('code', models.CharField(choices=[('CO', 'Cash On Delivery'), ('CH', 'Check / Money Order'), ('CC', 'Credit Card'), ('PO', 'Purchase Order')], max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sales_payment_method',
                'verbose_name_plural': 'Payment Methods',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(db_column='payment_method_code', on_delete=django.db.models.deletion.CASCADE, to='sales.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_orders', to='geo.Address'),
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set([('cart', 'product')]),
        ),
    ]
