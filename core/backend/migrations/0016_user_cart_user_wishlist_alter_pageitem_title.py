# Generated by Django 4.2.1 on 2023-06-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_alter_pageitem_image_alter_pageitem_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='cart', to='backend.productoption'),
        ),
        migrations.AddField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlist', to='backend.productoption'),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]