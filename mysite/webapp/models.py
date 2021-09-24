from datetime import datetime

from comtypes.automation import _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class news(models.Model):
    author = models.CharField(max_length=15)
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to="news image/")
    content = models.TextField()

    def __str__(self):
        return self.author


class workers(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    emp_id = models.IntegerField()
    address = models.CharField(max_length=20)
    image = models.ImageField(upload_to="employee/")

    def __str__(self):
        return self.name


class CartItem(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Cars(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    def __str__(self):
        return self.car_model
