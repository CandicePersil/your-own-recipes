# Generated by Django 4.2 on 2023-07-08 15:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("your_own_recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="product",
            unique_together={("label", "type")},
        ),
    ]
