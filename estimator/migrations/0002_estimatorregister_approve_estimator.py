# Generated by Django 4.1.3 on 2022-12-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("estimator", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="estimatorregister",
            name="approve_estimator",
            field=models.BooleanField(default=False),
        ),
    ]
