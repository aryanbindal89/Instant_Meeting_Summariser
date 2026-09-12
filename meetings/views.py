
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Meeting, ActionItem
from .services import (
    transcribe_audio,
    analyze_meeting,
    ask_meeting,
)


@login_required
def create_meeting(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        tags = request.POST.get("tags", "").strip()
        audio = request.FILES.get("audio")

        Meeting.objects.create(
            user=request.user,
            title=title,
            description=description,
            tags=tags,
            audio=audio,
        )

        return redirect("dashboard")

    return render(
        request,
        "meetings/create_meeting.html",
    )


@login_required
def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user,
    )

    return render(
        request,
        "meetings/meeting_detail.html",
        {"meeting": meeting},
    )


@login_required
def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user,
    )

    if request.method == "POST":
        meeting.title = request.POST.get(
            "title",
            "",
        ).strip()

        meeting.description = request.POST.get(
            "description",
            "",
        ).strip()

        meeting.tags = request.POST.get(
            "tags",
            "",
        ).strip()

        audio = request.FILES.get("audio")

        if audio:
            meeting.audio = audio

        meeting.save()

        return redirect(
            "meeting_detail",
            meeting_id=meeting.id,
        )

    return render(
        request,
        "meetings/edit_meeting.html",
        {"meeting": meeting},
    )


@login_required
def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user,
    )

    if request.method == "POST":
        meeting.delete()
        return redirect("dashboard")

    return render(
        request,
        "meetings/delete_meeting.html",
        {"meeting": meeting},
    )


@login_required
def transcribe_meeting(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user,
    )

    if not meeting.audio:
        return redirect(
            "meeting_detail",
            meeting_id=meeting.id,
        )

    transcript = transcribe_audio(
        meeting.audio.path
    )

    meeting.transcript = transcript
    meeting.save()

    return redirect(
        "meeting_detail",
        meeting_id=meeting.id,
    )


@login_required
def analyze_meeting_view(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user,
    )

    if not meeting.transcript:
        return redirect(
            "meeting_detail",
            meeting_id=meeting.id,
        )

    # Ask Gemini to analyze the transcript.
    analysis = analyze_meeting(
        meeting.transcript
    )

    # Store each AI section separately.
    sections = {
        "summary": "",
        "key_points": "",
        "action_items": "",
        "decisions": "",
    }

    current_section = None

    for line in analysis.splitlines():

        line = line.strip()

        if not line:
            continue

        normalized_line = line.upper()

        if normalized_line == "SUMMARY:":
            current_section = "summary"

        elif normalized_line == "KEY POINTS:":
            current_section = "key_points"

        elif normalized_line == "ACTION ITEMS:":
            current_section = "action_items"

        elif normalized_line == "DECISIONS:":
            current_section = "decisions"

        elif current_section:
            sections[current_section] += line + "\n"

    # Save AI analysis.
    meeting.summary = sections["summary"].strip()
    meeting.key_points = sections["key_points"].strip()
    meeting.action_items = sections["action_items"].strip()
    meeting.decisions = sections["decisions"].strip()

    meeting.save()

    # Remove old structured action items.
    # This prevents duplicates when the meeting
    # is analyzed again.
    ActionItem.objects.filter(
        meeting=meeting
    ).delete()

    # Create new structured action items.
    for line in sections["action_items"].splitlines():

        task = line.strip()

        # Remove common bullet characters.
        if task.startswith("-"):
            task = task[1:].strip()

        elif task.startswith("*"):
            task = task[1:].strip()

        elif task.startswith("•"):
            task = task[1:].strip()

        # Ignore empty tasks.
        if not task:
            continue

        ActionItem.objects.create(
            meeting=meeting,
            task=task,
        )

    return redirect(
        "meeting_detail",
        meeting_id=meeting.id,
    )


@login_required
def ask_meeting_view(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user,
    )

    if not meeting.transcript:
        return redirect(
            "meeting_detail",
            meeting_id=meeting.id,
        )

    if request.method == "POST":

        question = request.POST.get(
            "question",
            "",
        ).strip()

        if question:

            answer = ask_meeting(
                meeting.transcript,
                question,
            )

            # Make sure chat_history is always a list.
            if not isinstance(
                meeting.chat_history,
                list,
            ):
                meeting.chat_history = []

            meeting.chat_history.append(
                {
                    "question": question,
                    "answer": answer,
                }
            )

            meeting.save()

    return redirect(
        "meeting_detail",
        meeting_id=meeting.id,
    )


@login_required
def toggle_important(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user,
    )

    if request.method == "POST":
        meeting.is_important = not meeting.is_important
        meeting.save()

    return redirect(
        "meeting_detail",
        meeting_id=meeting.id,
    )


@login_required
def toggle_action_item(request, action_item_id):
    action_item = get_object_or_404(
        ActionItem,
        id=action_item_id,
        meeting__user=request.user,
    )

    if request.method == "POST":
        action_item.completed = not action_item.completed
        action_item.save()

    return redirect(
        "meeting_detail",
        meeting_id=action_item.meeting.id,
    )
