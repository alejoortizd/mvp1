from typing import Any

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django_filters.views import FilterView

from mvp.apps.collaborators.filters import CollaboratorFilter
from mvp.apps.collaborators.forms.collaborator import (
    CollaboratorForm,
    CollaboratorUpdateForm,
)
from mvp.apps.collaborators.models.collaborator import Collaborator
from mvp.apps.core.mixins import LoginRequiredAndOrganizationMixin


class CollaboratorListView(LoginRequiredAndOrganizationMixin, FilterView):
    model = Collaborator
    paginate_by = 10
    filterset_class = CollaboratorFilter

    def get_queryset(self):
        return super().get_queryset().filter(organization=self.request.user_organization)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class CollaboratorCreateView(LoginRequiredAndOrganizationMixin, CreateView):
    model = Collaborator
    form_class = CollaboratorForm
    template_name = "collaborators/collaborator_create.html"
    success_url = reverse_lazy("collaborator_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class CollaboratorUpdateView(LoginRequiredAndOrganizationMixin, UpdateView):
    model = Collaborator
    form_class = CollaboratorUpdateForm
    template_name = "collaborators/collaborator_update.html"
    success_url = reverse_lazy("collaborator_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


# class CollaboratorDeleteView(LoginRequiredAndOrganizationMixin, DeleteView):
#     model = Collaborator
#     template_name = "collaborator_confirm_delete.html"
#     success_url = reverse_lazy("collaborator_list")
