from django.db import models

class Officer(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown'),
    ]

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default="unknown")
    rank = models.CharField(max_length=100)
    badge_number = models.IntegerField(unique=True)
    area = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    nationality = models.CharField(max_length=255, default="Nigerian")

    def __str__(self):
        return self.name
