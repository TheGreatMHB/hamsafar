from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# User (Profile)
#Destination(Places)
#Entertainment(Actions)

class Profile(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    gender_choices = (
        ('M','Male'),
        ('F','Female')
    )
    name = models.CharField(max_length=100)
    age =  models.IntegerField()
    sex = models.CharField(choices=gender_choices)

class Destination (models.Model):
    address = models.TextField(max_length=500)

class Entertainment (models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.TimeField()
    price = models.DecimalField()

class Order (models.Model):
    client = models.ForeignKey(Profile,on_delete=models.CASCADE)
    place =  models.ForeignKey(Destination,on_delete=models.CASCADE)
    activity = models.ForeignKey(Entertainment,on_delete=models.CASCADE)
    price = client = models.ForeignKey(Profile,on_delete=models.CASCADE)
    duration = client = models.ForeignKey(Profile,on_delete=models.CASCADE)