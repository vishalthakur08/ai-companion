import json
import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

def extract_json(text: str):
    if not text or not text.strip():
        raise ValueError("LLM returned empty response")

    text = text.strip()
    text = text.replace("```json", "").replace("```", "").strip()

    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try to extract the first JSON object from a messy response
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group(0))

    raise ValueError(f"Could not parse JSON from response: {text[:500]}")
    return extract_json(content)



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
