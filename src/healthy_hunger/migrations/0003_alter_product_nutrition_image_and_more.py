# Generated by Django 4.2.6 on 2023-10-23 23:01

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('healthy_hunger', '0002_query_alter_product_nutrition_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutrition_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, scale=None, size=[700, 1350], upload_to='nutrition/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, scale=None, size=[600, 400], upload_to='product/'),
        ),
    ]
