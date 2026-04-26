"""Entry point for the AI Support Copilot."""
from src.copilot import analyze_ticket
from src.utils import banner, load_tickets, save_results
from src.logging_config import setup_logging


INPUT_FILE = "data/tickets.json"
OUTPUT_FILE = "data/results.json"

logger = setup_logging()


def process_batch() -> None:
    """Load tickets, analyze each, save results, log progress."""
    banner("AI SUPPORT COPILOT — BATCH MODE")
    
    logger.info(f"Starting batch from {INPUT_FILE}")
    
    try:
        tickets = load_tickets(INPUT_FILE)
    except FileNotFoundError as e:
        logger.error(f"Cannot start batch: {e}")
        return
    
    logger.info(f"Loaded {len(tickets)} tickets")
    
    results = []
    success_count = 0
    failure_count = 0
    
    for ticket in tickets:
        ticket_id = ticket.get("id", "UNKNOWN")
        
        try:
            analysis = analyze_ticket(ticket["text"])
            results.append({
                "ticket_id": ticket_id,
                "customer_email": ticket.get("customer_email"),
                "analysis": analysis,
                "status": "success",
            })
            success_count += 1
            logger.info(f"Analyzed {ticket_id}: {analysis['category']}/{analysis['urgency']}")
        except KeyError as e:
            results.append({
                "ticket_id": ticket_id,
                "error": f"Missing field: {e}",
                "status": "failed",
            })
            failure_count += 1
            logger.warning(f"Skipped {ticket_id}: missing field {e}")
        except Exception as e:
            results.append({
                "ticket_id": ticket_id,
                "error": str(e),
                "status": "failed",
            })
            failure_count += 1
            logger.error(f"Failed {ticket_id}: {e}")
    
    save_results(results, OUTPUT_FILE)
    
    banner("BATCH COMPLETE")
    logger.info(f"Batch complete — Successful: {success_count}, Failed: {failure_count}")
    logger.info(f"Output written to {OUTPUT_FILE}")


if __name__ == "__main__":
    process_batch()