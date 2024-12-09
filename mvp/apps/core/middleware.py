from mvp.apps.users.models.user import UserOrganization


class OrganizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user_organization = None
        organization_id = request.COOKIES.get("organizationid", None)
        if request.user.is_authenticated and organization_id is not None:
            try:
                user_organizations = request.user.user_organizations.get(organization__id=organization_id)
                request.user_organization = user_organizations.organization
            except (ValueError, TypeError):
                request.user_organization = None
            except UserOrganization.DoesNotExist:
                request.user_organization = None
        response = self.get_response(request)
        return response
