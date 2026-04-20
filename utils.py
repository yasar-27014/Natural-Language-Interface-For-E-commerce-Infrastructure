import time

def display_banner():
    print("\n" + "=" * 50)
    print("     SHOPEASE — E-COMMERCE CHATBOT")
    print("     Your 24/7 Shopping Assistant")
    print("=" * 50)
    print("  Welcome! How can I help you today?")

def display_help():
    print("\n" + "-" * 50)
    print("  WHAT YOU CAN ASK ME:")
    print("-" * 50)
    commands = [
        ("order status",  "Track your current order"),
        ("cancel order",  "How to cancel an order"),
        ("return",        "Return and refund policy"),
        ("payment",       "Payment methods available"),
        ("shipping",      "Delivery time and charges"),
        ("offers",        "Current deals and coupons"),
        ("support",       "Contact customer care"),
        ("help",          "Show this list"),
        ("exit",          "Close the chatbot"),
    ]
    for cmd, desc in commands:
        print(f"  {cmd:<18} {desc}")
    print("-" * 50)

def format_bot_reply(message):
    time.sleep(0.3)
    print()
    print("  Bot:")
    print("  " + "-" * 46)
    for line in message.split("\n"):
        print(f"  {line}")
    print("  " + "-" * 46)