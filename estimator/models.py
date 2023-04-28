from django.db import models

# Create your models here.


class estimatorRegister(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    phoneno = models.PositiveBigIntegerField()
    Dateofbirth = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    approve_estimator = models.BooleanField(default=False)