# Generated by Django 4.0.7 on 2023-02-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapapp', '0002_lab_test1'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab_test1',
            name='output',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
