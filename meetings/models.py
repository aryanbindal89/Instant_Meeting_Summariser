
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
