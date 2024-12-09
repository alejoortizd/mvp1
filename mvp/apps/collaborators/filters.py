from typing import List

import django_filters
from django import forms
from django.db.models import Q

from mvp.apps.collaborators.models.collaborator import Collaborator
from mvp.apps.core.constants import SEARCH_INPUT_CLASS


class CollaboratorFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method="filter_search",
        label="Search",
        widget=forms.TextInput(
            attrs={
                "class": SEARCH_INPUT_CLASS,
                "placeholder": "Buscar por nombre, cargo o departamento...",
            }
        ),
    )

    class Meta:
        model = Collaborator
        fields: List[str] = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(email__icontains=value)
        )
