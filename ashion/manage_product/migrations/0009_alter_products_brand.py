# Generated by Django 5.0.1 on 2024-02-09 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_category", "0006_rename_subcategory_category"),
        ("manage_product", "0008_products_priority_alter_products_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="brand",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="manage_category.brand",
            ),
        ),
    ]
