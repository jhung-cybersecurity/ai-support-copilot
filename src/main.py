"""Entry point for the AI Support Copilot."""
from src.copilot import analyze_ticket
from src.utils import banner, format_analysis


# Sample tickets for demonstration
SAMPLE_TICKETS = [
    {
        "id": "T-001",
        "text": "I can't log in. The site keeps showing a 500 error. I have a meeting in 30 minutes!",
    },
    {
        "id": "T-002",
        "text": "My subscription was charged twice this month. Please refund the duplicate charge.",
    },
    {
        "id": "T-003",
        "text": "Would love to see a dark mode in the dashboard. Just a suggestion!",
    },
    {
        "id": "T-004",
        "text": "I don't want any help from you but I want you to know that your website's UI is very bad and very hard to navigate around."
    }
]


def run_demo() -> None:
    """Analyze each sample ticket and print results."""
    banner("AI SUPPORT COPILOT — DEMO")

    for ticket in SAMPLE_TICKETS:
        print(f"\n\nTicket {ticket['id']}")
        print(f"Original: {ticket['text']}\n")

        try:
            analysis = analyze_ticket(ticket["text"])
            print(format_analysis(analysis))
        except Exception as e:
            print(f"  ERROR: {e}")


if __name__ == "__main__":
    run_demo()