# Generated by Django 4.1.7 on 2023-03-15 14:19

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=product.models.upload_image_to_products),
        ),
    ]
