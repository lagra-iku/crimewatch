from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from .models import AddNewOfficer

class OfficerBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            officer = AddNewOfficer.objects.get(username=username)
            if officer and check_password(password, officer.password):
                return officer
        except AddNewOfficer.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return AddNewOfficer.objects.get(pk=user_id)
        except AddNewOfficer.DoesNotExist:
            return None
