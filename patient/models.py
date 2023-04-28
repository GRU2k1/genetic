from django.db import models

# Create your models here.


class patientRegister(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    phoneno = models.PositiveBigIntegerField()
    Dateofbirth = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    admin_approve = models.BooleanField(default=False)
    second_approve= models.BooleanField(default=False)



class patient_detail(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    phone_no = models.PositiveBigIntegerField()
    Date_of_birth = models.CharField(max_length=20)
    Address = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Age = models.PositiveIntegerField()
    Marital_status = models.CharField(max_length=30)
    subject = models.CharField(max_length=250)
    send_basic_doctor = models.BooleanField(default=False)
    send_basic_lab = models.BooleanField(default=False)


class patient_medical_details(models.Model):
    name= models.CharField(max_length=50, null=True)
    Gender= models.CharField(max_length=50, null=True)
    age =  models.CharField(max_length=50, null=True)
    Martial_status= models.CharField(max_length=50, null=True)
    height = models.CharField(max_length=50, null=True)
    weight = models.CharField(max_length=50, null=True)
    blood_type = models.CharField(max_length=50, null=True)
    blood_count = models.CharField(max_length=50, null=True)
    symptoms = models.CharField(max_length=50, null=True)
    send_medi_doctor = models.BooleanField(default=False)
    send_medi_lab = models.BooleanField(default=False)


class lab_test(models.Model):
    name = models.CharField(max_length=200)
    Genes_in_mothers_side = models.CharField(max_length=50)
    Inherited_from_father = models.CharField(max_length=50)
    Maternal_gene = models.CharField(max_length=50)
    Paternal_gene = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Birth_defects = models.CharField(max_length=50)
    WhiteBlood_cell_count = models.FloatField()
    Blood_test_result = models.CharField(max_length=50)
    test_date = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True, null=True)
    contact_no = models.PositiveBigIntegerField()
    send_doctor_lab_report = models.BooleanField(default=False)
    output = models.CharField(max_length=50, null=True)
    send= models.BooleanField(default=False)
    send2= models.BooleanField(default=False)
