from django.contrib import admin

from mvp.apps.core.admin import BaseAdmin
from mvp.apps.users.models.user import User, UserOrganization


@admin.register(User)
class UserAdmin(BaseAdmin):
    pass


@admin.register(UserOrganization)
class UserOrganizationAdmin(BaseAdmin):
    ordering = ("organization", "user")
