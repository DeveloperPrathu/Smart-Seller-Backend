# Generated by Django 4.2.2 on 2023-06-17 20:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_user_address_user_contact_no_user_district_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tx_amount', models.IntegerField(default=0)),
                ('payment_mode', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(max_length=5000)),
                ('tx_id', models.CharField(max_length=1000, null=True)),
                ('tx_status', models.CharField(choices=[('INITIATED', 'INITIATED'), ('PENDING', 'PENDING'), ('INCOMPLETE', 'INCOMPLETE'), ('FAILED', 'FAILED'), ('FLAGGED', 'FLAGGED'), ('USER_DROPPED', 'USER_DROPPED'), ('SUCCESS', 'SUCCESS'), ('CANCELLED', 'CANCELLED'), ('VOID', 'VOID')], max_length=100, null=True)),
                ('tx_time', models.CharField(max_length=500, null=True)),
                ('tx_msg', models.CharField(max_length=500, null=True)),
                ('from_cart', models.BooleanField(default=True)),
                ('pending_orders', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_set', to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_price', models.IntegerField(default=0)),
                ('tx_price', models.IntegerField(default=0)),
                ('delivery_price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('rating', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('ORDERED', 'ORDERED'), ('PACKED', 'PACKED'), ('SHIPPED', 'SHIPPED'), ('OUT_FOR_DELIVERY', 'OUT_FOR_DELIVERY'), ('DELIVERED', 'DELIVERED'), ('CANCELLED', 'CANCELLED')], default='ORDERED', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_set', to='backend.order')),
                ('product_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_options_set', to='backend.productoption')),
            ],
        ),
    ]