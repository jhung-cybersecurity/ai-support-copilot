"""Display and formatting helpers."""


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