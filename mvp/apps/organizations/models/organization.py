from django.db import models

from mvp.apps.core.models import BaseModel


class Organization(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    users = models.ManyToManyField("users.User", through="users.UserOrganization")

    def __str__(self) -> str:
        return f"{self.name}"
