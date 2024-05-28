from django.db import models
import random
import string
import bcrypt

def generate_case_number():
    """Helper function to generate a random case number for a criminal record"""
    letters = string.ascii_letters
    numbers = string.digits
    return ''.join(random.choices(letters, k=2)) + ''.join(random.choices(numbers, k=6))

def generate_random_password(length=8):
    """Generate a random password with letters and digits"""
    symbols = string.punctuation
    characters = string.ascii_letters + string.digits + symbols
    return ''.join(random.choices(characters, k=length))

class PoliceOfficers(models.Model):
    """Police Officer's personal information Class"""
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, default="unknown")
    rank = models.CharField(max_length=100)
    badge_number = models.IntegerField()
    area = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    nationality = models.CharField(max_length=255, default="Nigerian")

    def __str__(self):
        return f"{self.name}, Rank: {self.rank}, Badge Number: {self.badge_number}, Area: {self.area}"

class AddNewOfficer(models.Model):
    """Police Officer's personal information Class"""
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    rank = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    badge_number = models.IntegerField(unique=True)

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = generate_random_password()
        elif self.pk is None or 'password' in self.get_dirty_fields():  # Only hash if the password is new or changed
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        super(AddNewOfficer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.surname}, Username: {self.username}, Rank: {self.rank}, Badge Number: {self.badge_number}, Status: {self.status}"

class CriminalRecord(models.Model):
    """Criminal's personal information Class"""
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    tribe = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    gender = models.CharField(max_length=10)
    nin = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=100)
    distinctive_features = models.TextField(default="Scars, Tribal marks, Tattoos, Piercings, etc.")
    next_of_kin = models.CharField(max_length=255)
    finger_print = models.ImageField(upload_to='images/')
    mugshot = models.ImageField(upload_to='images/')
    known_aliases = models.CharField(max_length=255)
    associates = models.CharField(max_length=255)
    case_number = models.CharField(max_length=9, default=generate_case_number, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.surname}"
  
class Case(models.Model):
    """New case Class"""
    case_number = models.CharField(max_length=9, default=generate_case_number, unique=True)
    event_date = models.DateTimeField()
    crime_type = models.CharField(max_length=255)
    location_of_crime = models.CharField(max_length=255)
    case_description = models.TextField()
    associated_criminals = models.ForeignKey(CriminalRecord, on_delete=models.CASCADE)
    associated_case_files = models.FileField(upload_to='files/')
    witnesses = models.CharField(max_length=255)
    known_suspects = models.CharField(max_length=255)
    arrested_suspects = models.CharField(max_length=255)
    case_status = models.CharField(max_length=100)
    pictures_of_evidence = models.ImageField(upload_to='images/')
    case_officer = models.ForeignKey(PoliceOfficers, on_delete=models.CASCADE)

    def __str__(self):
        return f"Case Number: {self.case_number}, Case Type: {self.crime_type}, Case Status: {self.case_status}"