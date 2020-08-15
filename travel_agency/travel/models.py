from django.db import models
from django.contrib.auth.models import AbstractUser
from travel.constants import COUNTRIES_CHOICES
import os


class Global(models.Model):
    name = models.CharField(max_length=6, default="Global")

    def __str__(self):
        return self.name


class Continent(models.Model):
    CONTINENT_CHOICES = (
        ('AF', 'Africa'),
        ('NA', 'North America'),
        ('OC', 'Oceania'),
        ('AN', 'Antarctica'),
        ('AN', 'Asia'),
        ('EU', 'Europe'),
        ('SA', 'South America'),
    )

    name = models.CharField(max_length=2, choices=CONTINENT_CHOICES)
    globally = models.ForeignKey(
        Global, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=2, choices=COUNTRIES_CHOICES)
    continent = models.ForeignKey(
        Continent, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=15)
    country = models.ForeignKey(
        Country, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=15)
    standard = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=15)
    city = models.ForeignKey(
        City, on_delete=models.DO_NOTHING, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Trip(models.Model):
    TYPE_CHOICES = (
        ('BB', 'Bed & Breakfast'),
        ('HB', 'Breakfast & Dinner'),
        ('FB', 'Full Board (Breakfast, Lunch & Dinner'),
        ('AI', 'All Inclusive'),
    )

    image = models.ImageField(upload_to='photos', blank=True, null=True)
    name = models.CharField(max_length=30)
    airport = models.ForeignKey(
        Airport, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    hotel = models.ForeignKey(
        Hotel, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    departuredate = models.DateField(null=True, blank=True)
    returndate = models.DateField(null=True, blank=True)
    triptype = models.CharField(max_length=2, choices=TYPE_CHOICES)
    priceadult = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    pricechild = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    promoted = models.BooleanField(default=False)
    number_of_beds_adult = models.PositiveIntegerField(default=1)
    numberofbedschild = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



class SocialMedia(models.Model):

    pinterest = models.TextField(null=True, blank=True)
    facebook = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)