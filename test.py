import json

from ai.llm import generate_response
from ai.prompts import generate_layout_prompt

print("Creating prompt...")

prompt = generate_layout_prompt(
    screen_name="Order Tracking",
    description="Track a customer's multi-stop ride in real time.",
    user_type="Customer",
    platform="Mobile",
    region="Global",
)

print("Calling AI...")

response = generate_response(prompt)

print("\n✅ Response received!\n")

print(json.dumps(response, indent=2))

print("\n-----------")

print("Screen Goal:")
print(response["problem_summary"]["screen_goal"])

print("\n-----------")

print("Layout Directions:")

for index, direction in enumerate(response["layout_directions"], start=1):
    print(f"{index}. {direction['name']}")