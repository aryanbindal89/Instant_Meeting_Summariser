from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    audio = models.FileField(
        upload_to="meetings/audio/",
        blank=True,
        null=True
    )

    transcript = models.TextField(blank=True)

    summary = models.TextField(blank=True)
    key_points = models.TextField(blank=True)
    action_items = models.TextField(blank=True)
    decisions = models.TextField(blank=True)

    is_important = models.BooleanField(default=False)

    tags = models.CharField(
        max_length=300,
        blank=True
    )

    chat_history = models.JSONField(
        default=list,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ActionItem(models.Model):
    meeting = models.ForeignKey(
        Meeting,
        on_delete=models.CASCADE,
        related_name="structured_action_items"
    )

    task = models.CharField(max_length=300)

    assignee = models.CharField(
        max_length=150,
        blank=True
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )

    completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.task