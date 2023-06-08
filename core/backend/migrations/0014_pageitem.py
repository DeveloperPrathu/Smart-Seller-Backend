# Generated by Django 4.2.1 on 2023-06-08 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='product/')),
                ('viewtype', models.IntegerField(choices=[(1, 'BANNER'), (2, 'SWIPER'), (3, 'GRID')])),
                ('title', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pageitems_set', to='backend.category')),
                ('product_options', models.ManyToManyField(blank=True, to='backend.product')),
            ],
        ),
    ]
