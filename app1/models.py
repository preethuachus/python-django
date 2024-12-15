from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

class shipping(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

