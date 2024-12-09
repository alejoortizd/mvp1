from django.urls import path

from mvp.apps.collaborators.views import (
    CollaboratorCreateView,
    CollaboratorListView,
    CollaboratorUpdateView,
)

urlpatterns = [
    path("", CollaboratorListView.as_view(), name="collaborator_list"),
    path("create/", CollaboratorCreateView.as_view(), name="collaborator_create"),
    path("update/<int:pk>/", CollaboratorUpdateView.as_view(), name="collaborator_update"),
]
