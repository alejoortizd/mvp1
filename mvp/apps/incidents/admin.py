from django.contrib import admin

from mvp.apps.core.admin import BaseAdmin
from mvp.apps.incidents.models.incident import Incident
from mvp.apps.incidents.models.incident_type import IncidentType


@admin.register(Incident)
class IncidentAdmin(BaseAdmin):
    list_display = ("organization", "collaborator", "incident_type", "incident_date", "status", "severity")
    list_filter = ("organization", "status", "severity")
    search_fields = ("organization", "collaborator", "incident_type", "status", "severity")


@admin.register(IncidentType)
class IncidentTypeAdmin(BaseAdmin):
    list_display = ("organization", "name", "description")
    list_filter = ("organization",)
    search_fields = ("organization", "name", "description")
