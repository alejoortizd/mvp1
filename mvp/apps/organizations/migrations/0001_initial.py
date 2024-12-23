# Generated by Django 5.1.3 on 2024-11-29 17:38

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("restored_at", models.DateTimeField(blank=True, null=True)),
                ("transaction_id", models.UUIDField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrganizationDepartment",
            fields=[
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("restored_at", models.DateTimeField(blank=True, null=True)),
                ("transaction_id", models.UUIDField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "organization",
                    models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="organizations.organization"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
