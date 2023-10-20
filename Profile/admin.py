from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile


class UserProfileInline(admin.StackedInline):
    model = Profile


class NewUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
