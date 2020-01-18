
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='register/static/register/img/', blank=True)
    def __str__(self):
        return self.name

class drink(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='register/static/register/img/', blank=True)
    def __str__(self):
        return self.name

class delivary(models.Model):
    address = models.CharField(max_length=200)
    number = models.IntegerField()
    size = models.CharField(max_length=1)
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

class delivary2(models.Model):
    address = models.CharField(max_length=200)
    number = models.IntegerField()
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()


class table(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    phone1 = models.IntegerField()

class birthday(models.Model):
    date = models.DateField()
    number = models.IntegerField()
    phone1 = models.IntegerField()
    phone2 = models.IntegerField()





