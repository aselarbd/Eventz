from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class UserType(Enum):
    ADMIN = "admin"
    ORGANIZER = "organizer"
    ATTENDEE = "attendee"
    SPEAKER = "speaker"
    VENDOR = "vendor"
    STAFF = "staff"
    SPONSOR = "sponsor"


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    USER_TYPE_CHOICES = [(type, type.value) for type in UserType]
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default=UserType.ATTENDEE
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True
