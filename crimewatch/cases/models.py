from django.db import models
from officers.models import Officer

class CrimeType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CrimeSubcategory(models.Model):
    crime_type = models.ForeignKey(CrimeType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CriminalCase(models.Model):
    CASE_STATUS_CHOICES = [
        ('active', 'Active'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    case_number = models.CharField(max_length=12, unique=True, editable=False)  # Generated in save method
    event_date = models.DateTimeField()
    crime_type = models.ForeignKey(CrimeType, on_delete=models.CASCADE)
    crime_subcategory = models.ForeignKey(CrimeSubcategory, on_delete=models.CASCADE)
    location_of_crime = models.CharField(max_length=255)
    case_description = models.TextField()
    associated_case_files = models.ManyToManyField('self', blank=True)
    witnesses = models.TextField()
    known_suspects = models.TextField()
    arrested_suspects = models.TextField()
    case_status = models.CharField(max_length=12, choices=CASE_STATUS_CHOICES)
    pictures_of_evidence = models.ImageField(upload_to='images/', null=True)
    case_officer = models.ForeignKey(Officer, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.case_number:
            self.case_number = self._generate_case_number()
        super().save(*args, **kwargs)

    def _generate_case_number(self):
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

    def __str__(self):
        return self.case_number
