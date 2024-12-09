from django.db import models

from mvp.apps.core.models import BaseModel


class IncidentType(BaseModel):
    organization = models.ForeignKey("organizations.Organization", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
