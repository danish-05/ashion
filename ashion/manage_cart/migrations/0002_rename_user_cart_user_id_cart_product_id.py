# Generated by Django 5.0.2 on 2024-02-15 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_cart", "0001_initial"),
        ("manage_product", "0016_remove_products_stock_remove_variant_color_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="user",
            new_name="user_id",
        ),
        migrations.AddField(
            model_name="cart",
            name="product_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="manage_product.products",
            ),
        ),
    ]
