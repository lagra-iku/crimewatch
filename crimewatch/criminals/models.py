from django.db import models
import random
import string
from officers.models import Officer


def generate_case_number():
    """Helper function to generate a random case number for a criminal record"""
    letters = string.ascii_letters
    numbers = string.digits
    return ''.join(random.choices(letters, k=2)) + ''.join(random.choices(numbers, k=6))

class CriminalRecord(models.Model):
    """Criminal's personal information Class"""
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_arrest = models.DateField(auto_now_add=True)
    time_of_arrest = models.TimeField(auto_now_add=True)
    crime_committed = models.CharField(max_length=100, default="Grand Larceny", blank=False)
    tribe = models.CharField(max_length=100)
    religion = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=100)
    height_in_meters = models.FloatField()
    weight_in_kg = models.FloatField()
    gender = models.CharField(max_length=10)
    nin = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    distinctive_features = models.TextField(default="Scars, Tribal marks, Tattoos, Piercings, etc.")
    next_of_kin = models.CharField(max_length=255, blank=True)
    finger_print = models.ImageField(upload_to='images/', blank=True)
    mugshot = models.ImageField(upload_to='images/', blank=True)
    known_aliases = models.CharField(max_length=255, blank=True)
    associates = models.CharField(max_length=255, blank=True)
    arresting_officer = models.ForeignKey(Officer, on_delete=models.CASCADE, blank=True)
    case_number = models.CharField(max_length=9, default=generate_case_number, unique=True)
    is_incarcerated = models.BooleanField(default=True)
    is_wanted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.surname}, {self.arresting_officer}, {self.nin}, {self.case_number}, {self.date_of_birth}, {self.tribe}, {self.religion}, {self.marital_status}, {self.height_in_meters}, {self.weight_in_kg}"

  
class LogIn(models.Model):
    """Class to hold login information"""
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username}, {self.password}"