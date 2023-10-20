from .base_profile_model import BaseProfile
from .user_type_models import (
    AttendeesProfile,
    OrganizersProfile,
    SpeakersProfile,
    VendorsProfile,
    StaffProfile,
    SponsorsProfile,
)


class Profile(
    BaseProfile,
    AttendeesProfile,
    OrganizersProfile,
    SpeakersProfile,
    VendorsProfile,
    StaffProfile,
    SponsorsProfile,
):
    pass
