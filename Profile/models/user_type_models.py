from django.db import models


class AttendeesProfile(models.Model):
    ticket_number = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True


class OrganizersProfile(models.Model):
    organization_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class SpeakersProfile(models.Model):
    expertise = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class VendorsProfile(models.Model):
    company_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class StaffProfile(models.Model):
    staff_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True


class SponsorsProfile(models.Model):
    sponsor_level = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True
