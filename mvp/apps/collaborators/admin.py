from django.contrib import admin

from mvp.apps.collaborators.models.collaborator import Collaborator
from mvp.apps.core.admin import BaseAdmin


@admin.register(Collaborator)
class CollaboratorAdmin(BaseAdmin):
    list_display = (
        "organization",
        "department",
        "role",
        "first_name",
        "last_name",
        "email",
        "start_date",
        "end_date",
    )
    search_fields = (
        "organization",
        "department",
        "role",
        "first_name",
        "last_name",
        "email",
        "start_date",
        "end_date",
    )
    ordering = (
        "organization",
        "department",
        "role",
        "first_name",
        "last_name",
    )
