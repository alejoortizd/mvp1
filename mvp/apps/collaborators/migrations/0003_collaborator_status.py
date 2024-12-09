# Generated by Django 5.1.3 on 2024-11-29 21:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collaborators", "0002_rename_rol_collaborator_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="collaborator",
            name="status",
            field=models.CharField(
                choices=[("ACTIVE", "Active"), ("INACTIVE", "Inactive")], default="ACTIVE", max_length=20
            ),
        ),
    ]