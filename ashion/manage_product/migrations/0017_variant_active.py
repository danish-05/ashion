# Generated by Django 5.0.2 on 2024-03-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_product", "0016_remove_products_stock_remove_variant_color_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="variant",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
