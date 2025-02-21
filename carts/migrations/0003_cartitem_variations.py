# Generated by Django 5.1 on 2025-02-19 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0002_rename_qantity_cartitem_quantity"),
        ("store", "0002_variation"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="variations",
            field=models.ManyToManyField(blank=True, to="store.variation"),
        ),
    ]
