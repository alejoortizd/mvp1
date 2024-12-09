from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django_filters.views import FilterView

from mvp.apps.organizations.models.organization import Organization
from mvp.apps.users.filters import SelectOrganizationFilter
from mvp.apps.users.models.user import UserOrganization


class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    next_page = "dashboard"
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())

        user = form.get_user()
        if user.organizations.exists():
            return HttpResponseRedirect("/auth/select_organization")
        return HttpResponseRedirect("/auth/login")


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    next_page = "login"


class SelectOrganizationView(LoginRequiredMixin, FilterView):
    model = UserOrganization
    paginate_by = 10
    template_name = "auth/select_organization.html"
    filterset_class = SelectOrganizationFilter

    def get_queryset(self):
        return self.request.user.user_organizations.all()

    def post(self, request, *args, **kwargs):
        organization = Organization.objects.get(id=request.POST.get("organization"))
        response = redirect("dashboard")
        response.set_cookie(
            "organizationid",
            organization.id,
            max_age=3600 * 24 * 7,
            samesite="Strict",
        )
        return response
