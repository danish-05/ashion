# Generated by Django 5.0.2 on 2024-02-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_order", "0007_cancelledorder_user_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderedproducts",
            name="status",
            field=models.CharField(
                choices=[
                    ("Order confirmed", "Order confirmed"),
                    ("Shipped", "Shipped"),
                    ("Out for delivery", "Out for delivery"),
                    ("Delivered", "Delivered"),
                    ("Cancelled", "Cancelled"),
                ]
            ),
        ),
    ]
