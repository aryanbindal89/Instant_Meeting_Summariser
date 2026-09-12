from django.contrib import admin
from .models import Meeting, ActionItem


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("title", "description", "user__username")


admin.site.register(ActionItem)