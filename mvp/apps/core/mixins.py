from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class LoginRequiredAndOrganizationMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user_organization is None:
            return redirect("select_organization")
        return super().dispatch(request, *args, **kwargs)


class ManagerGroupRequiredMixin:
    """Mixin that ensures the user is in the 'Managers' group."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name="Managers").exists():
            raise PermissionDenied  # Or return redirect('403') for a custom 403 page
        return super().dispatch(request, *args, **kwargs)
