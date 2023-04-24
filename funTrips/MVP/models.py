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
    sex = models.CharField(max_length=6,choices=gender_choices)

class Destination (models.Model):
    name = models.CharField(max_length=100,default='place_name')
    address = models.TextField(max_length=500,default='plcae_add')
    phone = models.IntegerField(default='09123456789')


class Entertainment (models.Model):
    type_choices = (
        ('Food','Food'),
        ('Exciting','Exciting'),
        ('Sport','Sport'),
        ('Relaxtion','Relaxtion'),
    )

    place = models.ForeignKey(Destination,on_delete=models.CASCADE,default='9999')
    name = models.CharField(max_length=100)
    type = models.CharField(choices=type_choices,max_length=100)
    duration = models.TimeField()
    price = models.DecimalField(max_digits=12,decimal_places=3)

class Order (models.Model):
    client = models.ForeignKey(Profile,on_delete=models.CASCADE)
    place =  models.ForeignKey(Destination,on_delete=models.CASCADE)
    activity = models.ForeignKey(Entertainment,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    duration = models.TimeField()