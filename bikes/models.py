from django.db import models


class Bike(models.Model):
    bike = models.CharField(max_length=5)
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('rented', 'Rented')])

