from django.db import models

from mvp.apps.collaborators.choices import CollaboratorStatus
from mvp.apps.core.models import BaseModel


class Collaborator(BaseModel):
    supervisor = models.ForeignKey(
        "collaborators.Collaborator", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="subordinates"
    )
    organization = models.ForeignKey("organizations.Organization", on_delete=models.DO_NOTHING)
    department = models.ForeignKey(
        "organizations.OrganizationDepartment", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    role = models.ForeignKey("organizations.OrganizationRole", on_delete=models.DO_NOTHING, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Not unique because a collaborator might me invited to another organization
    identification_number = models.CharField(max_length=30)
    email = models.EmailField()
    start_date = models.DateField(help_text="Date when the collaborator started working")
    end_date = models.DateField(null=True, blank=True, help_text="Date when the collaborator stopped working")
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        pass

    @property
    def status(self):
        if not self.end_date:
            return CollaboratorStatus.ACTIVE
        return CollaboratorStatus.INACTIVE
