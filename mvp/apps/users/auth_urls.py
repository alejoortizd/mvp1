from django.urls import path

from mvp.apps.users.views import (
    CustomLoginView,
    CustomLogoutView,
    SelectOrganizationView,
)

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("select_organization/", SelectOrganizationView.as_view(), name="select_organization"),
]
