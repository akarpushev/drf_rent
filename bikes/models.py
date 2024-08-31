from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Bike(models.Model):
    bike = models.CharField(max_length=5)
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('rented', 'Rented')])


class Rent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bike = models.OneToOneField(Bike, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)