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

    chat_history = models.JSONField(
        default=list,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title