from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from simple_history.models import HistoricalRecords

from mvp.apps.core.models import BaseModel


class UserOrganization(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_organizations")
    organization = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="user_organizations"
    )
    groups = models.ManyToManyField(Group, null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        unique_together = ("user", "organization")

    def __str__(self):
        return f"{self.organization} - {self.user}"


class User(AbstractUser, BaseModel):
    history = HistoricalRecords()
