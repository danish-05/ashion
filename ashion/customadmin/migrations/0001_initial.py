# Generated by Django 5.0.2 on 2024-03-06 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("manage_category", "0007_category_is_listed"),
        ("manage_product", "0018_rename_active_variant_is_listed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category_Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("percentage", models.FloatField(blank=True, default=0, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "category_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="manage_category.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product_Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("percentage", models.FloatField(blank=True, default=0, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "product_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="manage_product.products",
                    ),
                ),
            ],
        ),
    ]
