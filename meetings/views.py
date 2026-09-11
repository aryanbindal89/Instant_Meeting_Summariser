
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meeting
from .services import transcribe_audio

@login_required
def create_meeting(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        audio = request.FILES.get("audio")

        Meeting.objects.create(
            user=request.user,
            title=title,
            description=description,
            audio=audio
        )

        return redirect("dashboard")

    return render(
        request,
        "meetings/create_meeting.html"
    )


@login_required
def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user
    )

    return render(
        request,
        "meetings/meeting_detail.html",
        {"meeting": meeting}
    )


@login_required
def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user
    )

    if request.method == "POST":
        meeting.title = request.POST.get("title")
        meeting.description = request.POST.get("description")

        audio = request.FILES.get("audio")

        if audio:
            meeting.audio = audio

        meeting.save()

        return redirect(
            "meeting_detail",
            meeting_id=meeting.id
        )

    return render(
        request,
        "meetings/edit_meeting.html",
        {"meeting": meeting}
    )


@login_required
def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user
    )

    if request.method == "POST":
        meeting.delete()
        return redirect("dashboard")

    return render(
        request,
        "meetings/delete_meeting.html",
        {"meeting": meeting}
    )


@login_required
def transcribe_meeting(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user
    )

    if not meeting.audio:
        return redirect("meeting_detail", meeting_id=meeting.id)

    transcript = transcribe_audio(
        meeting.audio.path
    )

    meeting.transcript = transcript
    meeting.save()

    return redirect(
        "meeting_detail",
        meeting_id=meeting.id
    )