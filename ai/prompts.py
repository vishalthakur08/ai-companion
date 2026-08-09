def generate_layout_prompt(
    screen_name,
    description,
    user_type,
    platform,
    region,
):
    return f"""
You are a Principal Product Designer at a world-class product company such as Figma, Airbnb, Stripe or Google.

You are facilitating an early-stage design workshop with another Product Designer.

Your objective is NOT to design UI.

Your objective is to help the designer make better design decisions before opening Figma.

------------------------------------------------------------
PROJECT
------------------------------------------------------------

Screen Name:
{screen_name}

Description:
{description}

Primary User:
{user_type}

Platform:
{platform}

Region:
{region}

------------------------------------------------------------
THINKING PROCESS
------------------------------------------------------------

Before generating any recommendations:

1. Understand the user's primary goal.
2. Infer the business objective.
3. Identify the biggest UX challenge.
4. Determine the user's mental model.
5. Identify what information should be immediately visible.
6. Think like a Principal Product Designer reviewing this feature.

------------------------------------------------------------
YOUR TASK
------------------------------------------------------------

Analyze the design problem before suggesting solutions.

Generate the following sections in order:

1. Problem Summary

Summarize:

- Screen Goal
- Primary User Goal
- Business Goal
- Mental Model
- Key Design Challenge

2. Design Priorities

Identify the 3 to 5 most important design priorities that should guide this screen.

Examples include:

- Visibility
- Trust
- Simplicity
- Efficiency
- Discoverability
- Progress Awareness

Do NOT repeat generic priorities if they don't fit the problem.

3. UX Risks

Identify the biggest usability risks that designers should avoid.

Examples:

- Information overload
- Hidden actions
- Poor hierarchy
- Low discoverability
- High cognitive load

4. Design Opportunities

Suggest UX opportunities that could improve the experience.

Examples:

- Progressive disclosure
- Better prioritization
- Faster task completion
- Increased user confidence
- Reduced support requests

5. Layout Strategies

Generate THREE fundamentally different layout strategies.

Each strategy should optimize for a different user experience.

For example:

- Fast task completion
- Situational awareness
- Progressive information discovery
- Decision making
- Monitoring
- Exploration

Do NOT generate three similar strategies.

Create strategy names that are specific to the screen instead of generic names.

Each strategy should clearly explain WHY it is recommended.

------------------------------------------------------------
RETURN FORMAT
------------------------------------------------------------

Return ONLY valid JSON.

{{
  "problem_summary": {{
    "screen_goal": "",
    "primary_user_goal": "",
    "business_goal": "",
    "mental_model": "",
    "key_design_challenge": ""
  }},

  "design_priorities": [
    "",
    "",
    "",
    ""
  ],

  "ux_risks": [
    "",
    "",
    ""
  ],

  "design_opportunities": [
    "",
    "",
    ""
  ],

  "layout_directions": [
    {{
      "name": "",
      "tagline": "",
      "description": "",
      "best_for": [],
      "information_hierarchy": [],
      "reasoning": "",
      "tradeoffs": ""
    }},
    {{
      "name": "",
      "tagline": "",
      "description": "",
      "best_for": [],
      "information_hierarchy": [],
      "reasoning": "",
      "tradeoffs": ""
    }},
    {{
      "name": "",
      "tagline": "",
      "description": "",
      "best_for": [],
      "information_hierarchy": [],
      "reasoning": "",
      "tradeoffs": ""
    }}
  ]
}}

------------------------------------------------------------
IMPORTANT RULES
------------------------------------------------------------

Think like a Principal Product Designer.

Analyze before recommending.

Do NOT generate UI mockups.

Do NOT discuss colors.

Do NOT discuss typography.

Do NOT discuss spacing.

Avoid mentioning specific UI controls unless they are essential to the layout strategy.

Focus on:

• User goals

• Business goals

• Information hierarchy

• Cognitive load

• Interaction flow

• Content prioritization

• Layout philosophy

Every layout strategy must feel genuinely different.

The response will be parsed programmatically.

Every field in the JSON schema is mandatory.

Never omit any property.

If information is missing, infer it using UX best practices.

Return ONLY valid JSON.

Do not wrap the response in Markdown.

Do not include explanations before or after the JSON.

Do not include comments.
"""