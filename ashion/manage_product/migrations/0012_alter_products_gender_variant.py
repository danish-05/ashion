# Generated by Django 5.0.2 on 2024-02-13 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_product", "0011_alter_products_img1_alter_products_img2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="gender",
            field=models.CharField(
                choices=[("Men", "Men"), ("Women", "Women"), ("Kids", "Kids")],
                default="all",
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="Variant",
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
                (
                    "size",
                    models.CharField(
                        blank=True,
                        choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")],
                        max_length=5,
                        null=True,
                    ),
                ),
                (
                    "stock",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True, default="white", max_length=20, null=True
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="manage_product.products",
                    ),
                ),
            ],
        ),
    ]
