RESPONSES = [
    {
        "keywords": ["order status", "track order", "show status", "where is my order"],
        "response": (
            "ORDER STATUS\n"
            "  Your order #ORD-20481 is: OUT FOR DELIVERY\n"
            "  Estimated delivery: Today by 8:00 PM\n"
            "  Tracking ID: DL-77492-IN"
        )
    },
    {
        "keywords": ["cancel", "cancel order", "stop order"],
        "response": (
            "CANCEL ORDER\n"
            "  You can cancel within 24 hours of placing.\n"
            "  Go to: My Orders → Select Order → Cancel"
        )
    },
    {
        "keywords": ["return", "refund", "money back", "exchange"],
        "response": (
            "RETURNS & REFUNDS\n"
            "  Return window: 7 days from delivery\n"
            "  Refund time: 5-7 business days\n"
            "  Email: returns@shopease.in"
        )
    },
    {
        "keywords": ["payment", "pay", "upi", "credit card", "cod", "emi"],
        "response": (
            "PAYMENT OPTIONS\n"
            "  [+] UPI (Google Pay, PhonePe, Paytm)\n"
            "  [+] Credit / Debit Cards\n"
            "  [+] Cash on Delivery (orders under Rs.5000)\n"
            "  [+] EMI available on select cards"
        )
    },
    {
        "keywords": ["shipping", "delivery", "how long", "when will"],
        "response": (
            "SHIPPING INFO\n"
            "  Standard: 3-5 days (FREE above Rs.499)\n"
            "  Express : 1-2 days (Rs.99 extra)\n"
            "  Same Day: Metro cities only (Rs.149)"
        )
    },
    {
        "keywords": ["offer", "discount", "coupon", "deal", "sale", "promo"],
        "response": (
            "CURRENT OFFERS\n"
            "  WELCOME20  -> 20% off your first order\n"
            "  FLASH50    -> Rs.50 off above Rs.500\n"
            "  UPIBACK10  -> 10% cashback on UPI payments"
        )
    },
    {
        "keywords": ["support", "contact", "help", "call", "complaint"],
        "response": (
            "CUSTOMER SUPPORT\n"
            "  Phone   : 1800-123-4567 (9AM - 9PM, Free)\n"
            "  Email   : support@shopease.in\n"
            "  Chat    : www.shopease.in/chat (24/7)"
        )
    },
]

FALLBACK = (
    "Sorry, I did not understand that.\n"
    "  Try: 'order status', 'payment', 'offers', 'support'\n"
    "  Or type 'help' to see all commands."
)

def get_response(user_input):
    normalized = user_input.lower().strip()
    for entry in RESPONSES:
        for keyword in entry["keywords"]:
            if keyword in normalized:
                return entry["response"]
    return FALLBACK