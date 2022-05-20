from django.db import models

# Create your models here.
class Relatives(models.Model):


    nombre = models.CharField(max_length=20)
    age = models.IntegerField()
    dob = models.DateField()
    