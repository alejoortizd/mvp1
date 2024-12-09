from typing import List

import django_filters
from django import forms
from django.db.models import Q

from mvp.apps.core.constants import SEARCH_INPUT_CLASS
from mvp.apps.organizations.models.organization import Organization


class SelectOrganizationFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method="filter_search",
        label="Search",
        widget=forms.TextInput(
            attrs={
                "class": SEARCH_INPUT_CLASS,
                "placeholder": "Buscar por nombre...",
            }
        ),
    )

    class Meta:
        model = Organization
        fields: List[str] = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value))
