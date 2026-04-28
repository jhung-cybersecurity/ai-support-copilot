# AI Support Copilot

> A production-pattern AI tool that analyzes customer support tickets in batch and returns structured triage data using the Anthropic Claude API.

Drop a JSON file of tickets in, run one command, and get back categorized urgency-ranked analysis with suggested responses and routing actions. Built with fault tolerance, audit logging, and AI guardrails for unauthorized commitments.

## Demo

Input (`data/tickets.json`):
```json
{
"id": "T-001",
"submitted_at": "2026-04-25T09:14:00Z",
"customer_email": "alice@example.com",
"text": "I can't log in. The site keeps showing a 500 error. I have a meeting in 30 minutes!"
}
```

Output (`data/results.json`):
```json
{
  "ticket_id": "T-001",
  "customer_email": "alice@example.com",
  "analysis": {
    "category": "technical",
    "urgency": "high",
    "summary": "Customer cannot log in due to a 500 error and has a time-sensitive meeting.",
    "suggested_response": "I'm so sorry for the trouble. I'm escalating this to our technical team right now to investigate the server error...",
    "next_action": "escalate"
  },
  "status": "success"
}
```

Run output:

============================================================
AI SUPPORT COPILOT — BATCH MODE
2026-04-26 12:14:12 [INFO] Starting batch from data/tickets.json
2026-04-26 12:14:12 [INFO] Loaded 4 tickets
2026-04-26 12:14:16 [INFO] Analyzed T-001: technical/high
2026-04-26 12:14:19 [INFO] Analyzed T-002: billing/high
2026-04-26 12:14:22 [INFO] Analyzed T-003: feature_request/low
2026-04-26 12:14:26 [INFO] Analyzed T-004: technical/medium
2026-04-26 12:14:26 [INFO] Batch complete — Successful: 4, Failed: 0

## Features

- **Batch ticket processing** — load N tickets from JSON, analyze each, save structured results
- **Five-field structured analysis** — category, urgency, summary, suggested response, next action
- **AI guardrails** — system prompt prevents unauthorized commitments (refunds, timelines, account access)
- **Custom routing taxonomy** — 5 next_actions including `acknowledge_only` for feedback-without-reply scenarios
- **Fault tolerance** — per-ticket try/except so one bad ticket doesn't kill the batch
- **Production logging** — dual-handler (console + persistent file) with severity levels and timestamps
- **Centralized config** — `.env`-based secrets, single source of truth for model/client

## Architecture

ai-support-copilot/
├── data/
│   ├── tickets.json       # input tickets
│   └── results.json       # generated analysis (gitignored)
├── logs/
│   └── copilot.log        # persistent audit trail (gitignored)
└── src/
├── config.py          # env loading, shared Claude client
├── prompts.py         # XML-tagged system prompt + helpers
├── copilot.py         # analyze_ticket() core logic
├── utils.py           # display + file I/O helpers
├── logging_config.py  # named logger, dual handlers
└── main.py            # batch entry point

Each module has one responsibility. Replace any one and the rest still works.

## Tech Stack

| Tool | Why |
|---|---|
| Python 3.14 | Standard for AI/ML tooling |
| Anthropic SDK (claude-opus-4-7) | Reliable structured output via XML-tagged prompts |
| python-dotenv | Industry standard for secrets management |
| `logging` (stdlib) | Production-grade observability without external deps |
| `pathlib` (stdlib) | Modern cross-platform file handling |

## Setup

```bash
# Clone
git clone https://github.com/jhung-cybersecurity/ai-support-copilot.git
cd ai-support-copilot

# Virtual environment
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
# source venv/bin/activate  # macOS/Linux

# Dependencies
pip install -r requirements.txt

# Configure secrets
cp .env.example .env
# Then edit .env and add your ANTHROPIC_API_KEY
```

## Usage

```bash
python -m src.main
```

Reads `data/tickets.json`, processes each ticket, writes `data/results.json`, appends to `logs/copilot.log`.

To process your own tickets, replace the contents of `data/tickets.json` with your data following the same schema (`id`, `customer_email`, `text`).

## Engineering Notes

**Why XML-tagged prompts?** Claude was trained to parse structured XML in system prompts. Tags like `<role>`, `<task>`, `<rules>` produce more reliable structured output than freeform instructions.

**Why guardrails?** Initial testing revealed Claude offering refunds without authority ("I'll process a refund for the $200 difference"). Added explicit rules forbidding unauthorized commitments. Real-world AI safety pattern.

**Why fault-tolerant batches?** A single malformed ticket should not kill a 10,000-ticket overnight run. Each ticket is processed in its own try/except with the failure logged for review.

**Why temperature is omitted?** Claude Opus 4.7 deprecated the `temperature` parameter (April 2026). Determinism is now controlled via prompt engineering — explicit enums and strict rules in the system prompt.

## Limitations & Next Steps

- **Single-threaded** — processes tickets sequentially; large batches would benefit from `asyncio` parallelism
- **No retry logic** — transient API failures mark a ticket as failed permanently; should add exponential backoff
- **No evaluation suite** — quality is human-verified per run; adding a labeled test set with automated quality scoring would harden it
- **No deployment** — runs locally; FastAPI wrapper + Docker would make it service-ready

## Author

Built as part of a structured AI engineering learning track.
[GitHub](https://github.com/[YOUR_GITHUB_USERNAME])