from django.db import models

# Create your models here.


class lapRegister(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    phoneno = models.PositiveBigIntegerField()
    Dateofbirth = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    approve_lab = models.BooleanField(default=False)

class lab_test1 (models.Model):
    name = models.CharField(max_length=200)
    Genes_in_mothers_side = models.CharField(max_length=50)
    Inherited_from_father = models.CharField(max_length=50)
    Maternal_gene = models.CharField(max_length=50)
    Paternal_gene = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Birth_defects = models.CharField(max_length=50)
    WhiteBlood_cell_count = models.FloatField()
    Blood_test_result = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True)
    contact_no = models.PositiveBigIntegerField()
    send_doctor_lab_report = models.BooleanField(default=False)
    output= models.CharField(max_length=50,null=True)