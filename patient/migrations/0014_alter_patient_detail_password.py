# Generated by Django 4.0.2 on 2023-03-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_lab_test_send2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_detail',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
