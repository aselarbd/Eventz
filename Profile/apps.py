from django.apps import AppConfig


class ProfileConfig(AppConfig):
    name = "Profile"
    verbose_name = "User Profiles"

    def ready(self):
        from . import signals
