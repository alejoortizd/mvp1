from django.shortcuts import render
from django.views import View

from mvp.apps.collaborators.models.collaborator import Collaborator
from mvp.apps.core.mixins import LoginRequiredAndOrganizationMixin
from mvp.apps.incidents.choices import IncidentStatus
from mvp.apps.incidents.models.incident import Incident


class DashboardView(LoginRequiredAndOrganizationMixin, View):
    def get(self, request):
        active_collaborators = Collaborator.objects.filter(
            organization=request.user_organization, end_date__isnull=True
        ).count()
        collaborators = Collaborator.objects.filter(organization=request.user_organization)

        active_incidents = Incident.objects.filter(
            organization=request.user_organization, status__in=[IncidentStatus.IN_PROGRESS, IncidentStatus.OPEN]
        ).count()
        incidents = Incident.objects.filter(
            organization=request.user_organization,
        )

        average_monthye_incidents = Incident.monthly_average_incidents(organization=request.user_organization)
        open_cases = Incident.objects.filter(organization=request.user_organization, status=IncidentStatus.OPEN).count()
        total_incidents = incidents.count()

        context = {
            "title": "Dashboards",
            "active_collaborators": active_collaborators,
            "collaborators": collaborators,
            "active_incidents": active_incidents,
            "incidents": incidents,
            "average_monthye_incidents": average_monthye_incidents,
            "open_cases": open_cases,
            "total_incidents": total_incidents,
        }
        return render(request, "dashboard.html", context=context)
