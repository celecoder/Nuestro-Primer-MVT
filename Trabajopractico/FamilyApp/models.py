from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    bday_date= models.DateField(auto_now_add=True)
