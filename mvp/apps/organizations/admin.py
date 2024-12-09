from django.contrib import admin

from mvp.apps.core.admin import BaseAdmin
from mvp.apps.organizations.models.department import OrganizationDepartment
from mvp.apps.organizations.models.organization import Organization
from mvp.apps.organizations.models.role import OrganizationRole


@admin.register(Organization)
class OrganizationAdmin(BaseAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(OrganizationDepartment)
class OrganizationDepartmentAdmin(BaseAdmin):
    list_display = ("organization", "name", "description")
    search_fields = ("organization", "name", "description")
    ordering = ("organization", "name")


@admin.register(OrganizationRole)
class OrganizationRoleAdmin(BaseAdmin):
    list_display = ("organization", "name", "description")
    search_fields = ("organization", "name", "description")
    ordering = ("organization", "name")
