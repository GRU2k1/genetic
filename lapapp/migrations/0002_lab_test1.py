# Generated by Django 4.0.7 on 2023-01-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lapapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lab_test1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Genes_in_mothers_side', models.CharField(max_length=50)),
                ('Inherited_from_father', models.CharField(max_length=50)),
                ('Maternal_gene', models.CharField(max_length=50)),
                ('Paternal_gene', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Birth_defects', models.CharField(max_length=50)),
                ('WhiteBlood_cell_count', models.FloatField()),
                ('Blood_test_result', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('contact_no', models.PositiveBigIntegerField()),
                ('send_doctor_lab_report', models.BooleanField(default=False)),
            ],
        ),
    ]