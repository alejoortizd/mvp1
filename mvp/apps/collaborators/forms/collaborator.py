from django import forms

from mvp.apps.collaborators.models.collaborator import Collaborator
from mvp.apps.core.constants import DATE_INPUT_CLASS, TEXT_INPUT_CLASS
from mvp.apps.organizations.models.organization import Organization


class CollaboratorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        self.fields["organization"].queryset = Organization.objects.filter(id=request.user_organization.id)
        self.fields["organization"].initial = request.user_organization

    class Meta:
        model = Collaborator
        fields = [
            "organization",
            "supervisor",
            "department",
            "role",
            "first_name",
            "last_name",
            "identification_number",
            "start_date",
            "date_of_birth",
            "email",
            "phone_number",
            "address",
        ]
        exclude = [
            "deleted_at",
            "restored_at",
            "transaction_id",
            "created_at",
            "updated_at",
        ]
        widgets = {
            "organization": forms.Select(attrs={"class": TEXT_INPUT_CLASS}),
            "supervisor": forms.Select(attrs={"class": TEXT_INPUT_CLASS}),
            "department": forms.Select(attrs={"class": TEXT_INPUT_CLASS}),
            "role": forms.Select(attrs={"class": TEXT_INPUT_CLASS}),
            "first_name": forms.TextInput(attrs={"class": TEXT_INPUT_CLASS}),
            "last_name": forms.TextInput(attrs={"class": TEXT_INPUT_CLASS}),
            "identification_number": forms.NumberInput(attrs={"class": TEXT_INPUT_CLASS}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": DATE_INPUT_CLASS}),
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": DATE_INPUT_CLASS}),
            "email": forms.EmailInput(attrs={"class": TEXT_INPUT_CLASS}),
            "phone_number": forms.NumberInput(attrs={"class": TEXT_INPUT_CLASS}),
            "address": forms.Textarea(attrs={"class": TEXT_INPUT_CLASS, "rows": 1}),
        }
        labels = {
            "supervisor": "Supervisor",
            "organization": "Empresa",
            "department": "Departamento",
            "role": "Cargo",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "identification_number": "Número de Indentificación",
            "start_date": "Fecha de Ingreso",
            "date_of_birth": "Fecha de Nacimiento",
            "email": "Correo",
            "phone_number": "Teléfono",
            "address": "Dirección",
        }


class CollaboratorUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        self.fields["organization"].queryset = Organization.objects.filter(id=request.user_organization.id)
        self.fields["organization"].initial = request.user_organization

    class Meta:
        model = Collaborator
        fields = [
            "organization",
            "supervisor",
            "department",
            "role",
            "first_name",
            "last_name",
            "identification_number",
            "start_date",
            "end_date",
            "date_of_birth",
            "email",
            "phone_number",
            "address",
        ]
        exclude = [
            "deleted_at",
            "restored_at",
            "transaction_id",
            "created_at",
            "updated_at",
        ]
        widgets = {
            "organization": forms.Select(attrs={"class": TEXT_INPUT_CLASS}),
            "supervisor": forms.Select(attrs={"class": TEXT_INPUT_CLASS}),
            "department": forms.Select(attrs={"class": TEXT_INPUT_CLASS}),
            "role": forms.Select(attrs={"class": TEXT_INPUT_CLASS}),
            "first_name": forms.TextInput(attrs={"class": TEXT_INPUT_CLASS}),
            "last_name": forms.TextInput(attrs={"class": TEXT_INPUT_CLASS}),
            "identification_number": forms.NumberInput(attrs={"class": TEXT_INPUT_CLASS}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": DATE_INPUT_CLASS}),
            "end_date": forms.DateInput(attrs={"type": "date", "class": DATE_INPUT_CLASS}),
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": DATE_INPUT_CLASS}),
            "email": forms.EmailInput(attrs={"class": TEXT_INPUT_CLASS}),
            "phone_number": forms.NumberInput(attrs={"class": TEXT_INPUT_CLASS}),
            "address": forms.Textarea(attrs={"class": TEXT_INPUT_CLASS, "rows": 1}),
        }
        labels = {
            "supervisor": "Supervisor",
            "organization": "Empresa",
            "department": "Departamento",
            "role": "Cargo",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "identification_number": "Número de Indentificación",
            "start_date": "Fecha de Ingreso",
            "end_date": "Fecha de Salida",
            "date_of_birth": "Fecha de Nacimiento",
            "email": "Correo",
            "phone_number": "Teléfono",
            "address": "Dirección",
        }
