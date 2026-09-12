
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Meeting
from .services import transcribe_audio, analyze_meeting, ask_meeting

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

@login_required
def analyze_meeting_view(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user
    )

    if not meeting.transcript:
        return redirect(
            "meeting_detail",
            meeting_id=meeting.id
        )

    analysis = analyze_meeting(
        meeting.transcript
    )

    # Split Gemini response into sections
    sections = {
        "summary": "",
        "key_points": "",
        "action_items": "",
        "decisions": ""
    }

    current_section = None

    for line in analysis.splitlines():
        line = line.strip()

        if line == "SUMMARY:":
            current_section = "summary"

        elif line == "KEY POINTS:":
            current_section = "key_points"

        elif line == "ACTION ITEMS:":
            current_section = "action_items"

        elif line == "DECISIONS:":
            current_section = "decisions"

        elif current_section:
            sections[current_section] += line + "\n"

    meeting.summary = sections["summary"].strip()
    meeting.key_points = sections["key_points"].strip()
    meeting.action_items = sections["action_items"].strip()
    meeting.decisions = sections["decisions"].strip()

    meeting.save()

    return redirect(
        "meeting_detail",
        meeting_id=meeting.id
    )

@login_required
def ask_meeting_view(request, meeting_id):
    meeting = get_object_or_404(
        Meeting,
        id=meeting_id,
        user=request.user
    )

    if not meeting.transcript:
        return redirect(
            "meeting_detail",
            meeting_id=meeting.id
        )

    if request.method == "POST":
        question = request.POST.get("question", "").strip()

        if question:
            answer = ask_meeting(
                meeting.transcript,
                question
            )

            meeting.chat_history.append({
                "question": question,
                "answer": answer
            })

            meeting.save()

    return redirect(
        "meeting_detail",
        meeting_id=meeting.id
    )