from django.db import models
from django.db.models import Count
from django.db.models.functions import TruncMonth

from mvp.apps.core.models import BaseModel
from mvp.apps.incidents.choices import IncidentSeverity, IncidentStatus


class Incident(BaseModel):
    organization = models.ForeignKey("organizations.Organization", on_delete=models.DO_NOTHING)
    collaborator = models.ForeignKey("collaborators.Collaborator", on_delete=models.DO_NOTHING)
    incident_type = models.ForeignKey("incidents.IncidentType", on_delete=models.DO_NOTHING)
    incident_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=20, choices=IncidentStatus.choices, default=IncidentStatus.OPEN)
    severity = models.CharField(max_length=20, choices=IncidentSeverity.choices, default=IncidentSeverity.LOW)

    def __str__(self):
        return f"{self.organization}: {self.collaborator}"

    @classmethod
    def monthly_average_incidents(cls, organization):
        monthly_incident_counts = (
            Incident.objects.filter(organization=organization)
            .annotate(month=TruncMonth("incident_date"))
            .values("month")
            .annotate(count=Count("id"))
            .order_by("month")
        )
        total_months = monthly_incident_counts.count()
        total_incidents = sum(month_data["count"] for month_data in monthly_incident_counts)
        return total_incidents / total_months if total_months else 0
