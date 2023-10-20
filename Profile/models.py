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


# Create your models here.


class Profile(models.Model):
    USER_TYPE_CHOICES = [(tag, tag.value) for tag in UserType]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default=UserType.ATTENDEE
    )
    email = models.EmailField(unique=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"( {self.user.username} )"
