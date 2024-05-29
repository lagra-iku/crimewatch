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
    middle_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_arrest = models.DateField(auto_now_add=True)
    time_of_arrest = models.TimeField(auto_now_add=True)
    tribe = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    height_in_meters = models.FloatField()
    weight_in_kg = models.FloatField()
    gender = models.CharField(max_length=10)
    nin = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    contact_info = models.CharField(max_length=100)
    distinctive_features = models.TextField(default="Scars, Tribal marks, Tattoos, Piercings, etc.")
    next_of_kin = models.CharField(max_length=255)
    finger_print = models.ImageField(upload_to='images/', blank=True)
    mugshot = models.ImageField(upload_to='images/', blank=True)
    known_aliases = models.CharField(max_length=255)
    associates = models.CharField(max_length=255, blank=True)
    arresting_officer = models.ForeignKey(Officer, on_delete=models.CASCADE, blank=True)
    case_number = models.CharField(max_length=9, default=generate_case_number, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.surname}, {self.arresting_officer}, {self.nin}, {self.case_number}, {self.date_of_birth}, {self.tribe}, {self.religion}, {self.marital_status}, {self.height_in_meters}, {self.weight_in_kg}"

  
