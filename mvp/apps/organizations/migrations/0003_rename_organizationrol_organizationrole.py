# Generated by Django 5.1.3 on 2024-11-29 18:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("organizations", "0002_organizationrol"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="OrganizationRol",
            new_name="OrganizationRole",
        ),
    ]
