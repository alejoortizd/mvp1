# Generated by Django 5.1.3 on 2024-11-29 18:09

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("organizations", "0003_rename_organizationrol_organizationrole"),
    ]

    operations = [
        migrations.CreateModel(
            name="Collaborator",
            fields=[
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("restored_at", models.DateTimeField(blank=True, null=True)),
                ("transaction_id", models.UUIDField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("last_checkup", models.DateField(blank=True, null=True)),
                ("next_checkup", models.DateField(blank=True, null=True)),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="organizations.organizationdepartment",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="organizations.organization"),
                ),
                (
                    "rol",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="organizations.organizationrole",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
