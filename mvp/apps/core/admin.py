from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at", "deleted_at", "restored_at", "transaction_id")
