# Generated by Django 5.0.6 on 2024-11-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="seasonalflavor",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="seasonalflavor",
            name="season",
            field=models.CharField(
                choices=[
                    ("Spring", "Spring"),
                    ("Summer", "Summer"),
                    ("Fall", "Fall"),
                    ("Winter", "Winter"),
                ],
                default="Spring",
                max_length=20,
            ),
        ),
    ]