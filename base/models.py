from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='username')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class ResourceType(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    description = models.TextField()

class Resource(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(ResourceType, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    quantity = models.IntegerField(null=True)
    department = models.ManyToManyField(Department)


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    company_name = models.CharField(max_length=200)
    contact_number = models.IntegerField()


class Purchase(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    resource = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()




