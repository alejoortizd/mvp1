# Generated by Django 5.1.3 on 2024-11-29 18:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("collaborators", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="collaborator",
            old_name="rol",
            new_name="role",
        ),
    ]