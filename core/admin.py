
from django.contrib import admin
from .models import Faculty, Notice, Event


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "qualification", "email")
    search_fields = ("name", "designation", "qualification")


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "venue")
    search_fields = ("title", "venue")
    ordering = ("event_date",)
