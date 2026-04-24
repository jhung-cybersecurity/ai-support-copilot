"""Core ticket analysis logic."""
import json
from src.config import client, MODEL, DEFAULT_MAX_TOKENS
from src.prompts import SYSTEM_PROMPT, build_ticket_prompt


def analyze_ticket(ticket_text: str) -> dict:
    """
    Analyze a support ticket and return structured data.
    
    Args:
        ticket_text: The raw support ticket from the customer
    
    Returns:
        dict with keys: category, urgency, summary, suggested_response, next_action
    """
    message = client.messages.create(
        model=MODEL,
        max_tokens=DEFAULT_MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": build_ticket_prompt(ticket_text)}
        ]
    )
    
    # Extract text from response
    response_text = message.content[0].text
    
    # Parse JSON
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Claude returned invalid JSON: {response_text}") from e