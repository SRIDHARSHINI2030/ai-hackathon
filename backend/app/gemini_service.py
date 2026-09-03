import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai import errors


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")


client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=120000),
)


def generate_response(prompt: str) -> str:
    max_attempts = 3

    for attempt in range(max_attempts):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
            )

            return response.text

        except errors.ServerError as error:
            if attempt == max_attempts - 1:
                raise

            print(
                f"Gemini server is temporarily unavailable. "
                f"Retrying ({attempt + 1}/{max_attempts - 1})..."
            )

            time.sleep(5)