from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model for storing user profile details
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(unique=True, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # Field to check if the user is active
    energy_usage = models.FloatField(default=0.0)  # Field to store the energy usage of the user

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Appliance(models.Model):
    appliances=models.CharField(max_length=100)
    power = models.FloatField(help_text="Power rating in watts")
    hours = models.FloatField(help_text="Daily usage in hours")
    days = models.FloatField(help_text="Days used in a month")

    def monthly_usage(self):
        return self.power * self.hours * self.days / 1000
    
    def __str__(self):
        return self.name