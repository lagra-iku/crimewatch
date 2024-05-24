from django.db import models

# Create your models here.
class PoliceOfficers(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, default="unknown")
    rank = models.CharField(max_length=100)
    badge_number = models.IntegerField()
    Area = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    # profile_picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name