from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_meeting, name="create_meeting"),
    path("<int:meeting_id>/edit/", views.edit_meeting, name="edit_meeting"),
    path("<int:meeting_id>/delete/", views.delete_meeting, name="delete_meeting"),
    path("<int:meeting_id>/", views.meeting_detail, name="meeting_detail"),
    path(
    "<int:meeting_id>/transcribe/",
    views.transcribe_meeting,
    name="transcribe_meeting"
),
path(
    "<int:meeting_id>/analyze/",
    views.analyze_meeting_view,
    name="analyze_meeting"
),

path("<int:meeting_id>/ask/", views.ask_meeting_view, name="ask_meeting"),
]