import os
import time

from google import genai
from google.genai import errors


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def transcribe_audio(audio_file):
    uploaded_file = client.files.upload(
        file=audio_file
    )

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-transcribe",
                contents=[uploaded_file]
            )

            for part in response.candidates[0].content.parts:
                if hasattr(part, "audio_transcription"):
                    return part.audio_transcription.text

            raise ValueError("No transcription found in Gemini response.")

        except errors.ServerError as e:
            if e.code == 503 and attempt < 2:
                time.sleep(5)
            else:
                raise


def analyze_meeting(transcript):
    prompt = f"""
You are an AI meeting assistant.

Analyze the following meeting transcript and return:

1. Summary
2. Key Points
3. Action Items
4. Decisions

Keep the information clear, concise, and useful.

Meeting Transcript:
{transcript}

Format your response exactly like this:

SUMMARY:
<summary>

KEY POINTS:
- point 1
- point 2

ACTION ITEMS:
- action item 1
- action item 2

DECISIONS:
- decision 1
- decision 2
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text