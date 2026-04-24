from src.copilot import analyze_ticket

test_ticket = """
I'm so very disappointed at your company right now. I paid for the product and your shipping team said it's shipped out but I waited 2 weeks now and still haven't gotten any response until today. Billing reached out and refunded me. Even though I got my money back, I still want to tell you guys that this is very disappointing and not okay. I've been a customer for 50 years and this is how you treat royal customers? I don't want anything from you guys, won't purchase from you guys again. Don't reach out to me at all.
"""

result = analyze_ticket(test_ticket)

print("=" * 50)
print("TICKET ANALYSIS")
print("=" * 50)
for key, value in result.items():
    print(f"\n{key.upper()}:")
    print(f"  {value}")