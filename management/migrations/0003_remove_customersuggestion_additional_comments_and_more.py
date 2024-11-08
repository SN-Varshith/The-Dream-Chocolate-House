# Generated by Django 5.0.6 on 2024-11-05 07:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0002_seasonalflavor_is_available_seasonalflavor_season"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customersuggestion",
            name="additional_comments",
        ),
        migrations.RemoveField(
            model_name="customersuggestion",
            name="allergy_info",
        ),
        migrations.RemoveField(
            model_name="customersuggestion",
            name="suggested_flavor",
        ),
        migrations.AddField(
            model_name="customersuggestion",
            name="allergy_concerns",
            field=models.CharField(default="None", max_length=200),
        ),
        migrations.AddField(
            model_name="customersuggestion",
            name="flavor_suggestion",
            field=models.CharField(default="No Suggestion", max_length=200),
        ),
        migrations.AddField(
            model_name="customersuggestion",
            name="submitted_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="customersuggestion",
            name="customer_name",
            field=models.CharField(max_length=100),
        ),
    ]
