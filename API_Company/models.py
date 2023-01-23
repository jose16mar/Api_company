from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    fundador = models.CharField(max_length=50)
    