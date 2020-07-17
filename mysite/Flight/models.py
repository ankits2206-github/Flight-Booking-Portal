from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Airport(models.Model):
    code=models.CharField(max_length=5)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"



class Flight(models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()


    def __str__(self):
        return f"{self.id}-{self.origin} to {self.destination}"


class Passenger(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    age = models.IntegerField(default=18)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")


    def __str__(self):
        return f"{self.first} {self.last}"


class Bookings(models.Model):
    bookedby = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bookedby")
    bookedfor = models.ForeignKey(Passenger,on_delete=models.CASCADE,related_name="bookedfor")
    route = models.ForeignKey(Flight,on_delete=models.CASCADE,related_name="bookedflight")
    date = models.DateField(default=date.today())



    def __str__(self):
        return f"Booked By -{self.bookedby.first_name} For {self.bookedfor}"


