"""Entry point for the AI Support Copilot."""
from src.copilot import analyze_ticket
from src.utils import banner, format_analysis, load_tickets, save_results

INPUT_FILE = "data/tickets.json"
OUTPUT_FILE = "data/results.json"

def process_batch() -> None:
    """Load tickets, analyze each, save results, print summary."""
    banner("AI SUPPORT COPILOT — BATCH MODE")

    tickets = load_tickets(INPUT_FILE)
    print(f"\nLoaded {len(tickets)} tickets from {INPUT_FILE}\n")

    results = []
    success_count = 0
    failure_count = 0

    for ticket in tickets:
        ticket_id = ticket["id"]
        print(f"Processing {ticket_id}...", end=" ", flush=True)

        try:
            analysis = analyze_ticket(ticket["text"])
            results.append({
                "ticket_id": ticket_id,
                "customer_email": ticket["customer_email"],
                "analysis": analysis,
                "status": "success",
            })
            success_count += 1
            print("✓")
        except Exception as e:
            results.append({
                "ticket_id": ticket_id,
                "customer_email": ticket["customer_email"],
                "error": str(e),
                "status": "failed",
            })
            failure_count += 1
            print(f"x ({e})")

    save_results(results, OUTPUT_FILE)

    banner("BATCH COMPLETE")
    print(f"\n Successful; {success_count}")
    print(f" Failed:    {failure_count}")
    print(f" Output:    {OUTPUT_FILE}\n")


if __name__ == "__main__":
    process_batch()