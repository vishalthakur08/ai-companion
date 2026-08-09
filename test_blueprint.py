import json

from ai.blueprint_prompt import generate_blueprint_prompt
from ai.llm import generate_response

print("Creating blueprint prompt...")

prompt = generate_blueprint_prompt(
    screen_name="Order Tracking",
    description="Track a customer's multi-stop ride in real time.",
    layout_strategy="The Hybrid Dashboard",
)

print("Calling AI...")

response = generate_response(prompt)

print(json.dumps(response, indent=2))