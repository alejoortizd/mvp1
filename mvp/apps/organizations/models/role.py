from django.db import models

from mvp.apps.core.models import BaseModel


class OrganizationRole(BaseModel):
    organization = models.ForeignKey("organizations.Organization", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"
