# Generated by Django 5.1 on 2025-01-28 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
