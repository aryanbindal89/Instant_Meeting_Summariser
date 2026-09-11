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