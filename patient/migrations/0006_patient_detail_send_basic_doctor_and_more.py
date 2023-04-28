# Generated by Django 4.0.7 on 2022-12-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_patient_medical_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_detail',
            name='send_basic_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient_medical_details',
            name='send_medi_doctor',
            field=models.BooleanField(default=False),
        ),
    ]