from django.db import models

# Create your models here.

class Customers(models.Model):
    # CustomerID = models.
    CompanyName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)