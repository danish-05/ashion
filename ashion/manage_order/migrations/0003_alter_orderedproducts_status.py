# Generated by Django 5.0.2 on 2024-02-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_order", "0002_alter_orderedproducts_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderedproducts",
            name="status",
            field=models.IntegerField(
                choices=[
                    ("Order confirmed", "Order confirmed"),
                    ("Shipped", "Shipped"),
                    ("Out for delivery", "Out for delivery"),
                    ("Delivered", "Delivered"),
                    ("Cancelled", "Cancelled"),
                    ("Cancell request send", "Cancell request send"),
                ]
            ),
        ),
    ]
