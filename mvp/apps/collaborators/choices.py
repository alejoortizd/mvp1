from django.db import models


class CollaboratorStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Activo"
    INACTIVE = "INACTIVE", "Inactivo"
