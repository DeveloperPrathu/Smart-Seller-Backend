# Generated by Django 4.2.1 on 2023-06-08 14:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_alter_product_id_productoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2fcc382f-790b-451a-9130-1ef531304e2b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productoption',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]
