"""Display and formatting helpers."""
import json
from pathlib import Path

def load_tickets(filepath: str) -> list:
    """Load tickets from a JSON file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Tickets file not found: {filepath}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_results(results: list, filepath: str) -> None:
    """Save analysis results to a JSON file."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def divider(char: str = "=", length: int = 60) -> None:
    """Print a horizontal divider line."""
    print(char * length)


def banner(title: str) -> None:
    """Print a centered banner with dividers above and below."""
    divider()
    print(title.center(60))
    divider()

def truncate(text: str, max_length: int = 80) -> str:
    """Shorten text to max_length, adding '...' if truncated."""
    if len(text) <= max_length:
        return text
    return text[0:max_length-3] + "..."

def format_analysis(analysis: dict) -> str:
    """Format a ticket analysis dict into readable text."""
    lines = []
    for key, value in analysis.items():
        label = key.replace("_", " ").upper()
        lines.append(f"\n{label}:")
        lines.append(f"  {value}")
    return "\n".join(lines)