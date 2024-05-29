from django.db import models

class Criminal(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    crime_committed = models.CharField(max_length=255)
    date_of_arrest = models.DateField(default=None, blank=True, null=True)
    is_incarcerated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.alias})"