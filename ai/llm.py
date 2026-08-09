import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


def generate_response(prompt: str):
    """
    Sends the prompt to OpenRouter and returns a Python dictionary.
    """

    print("Sending request...")

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openrouter/free",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        """

You are a Principal Product Designer.

You MUST strictly follow the user's requested JSON schema.

Do not omit any fields.

Return ONLY valid JSON.

Do not wrap the JSON inside markdown.

"""
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            "temperature": 0.7,
            "max_tokens": 2000,
        },
        timeout=30,
    )

    response.raise_for_status()

    print("Received response!")

    content = response.json()["choices"][0]["message"]["content"]

    # Remove markdown fences if the model wraps the JSON
    content = content.replace("```json", "").replace("```", "").strip()

    return json.loads(content)
