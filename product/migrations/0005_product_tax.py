# Generated by Django 4.1.7 on 2023-03-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.FloatField(null=True),
        ),
    ]
