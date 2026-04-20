from responses import get_response
from utils import display_banner, display_help, format_bot_reply

def run_chatbot():
    display_banner()
    print("  Type 'help' to see commands. Type 'exit' to quit.\n")
    print("-" * 50)

    while True:
        user_input = input("\n  You: ").strip()

        if not user_input:
            print("  Bot: Please type something! Try 'help'.")
            continue

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\n  Bot: Thank you! Goodbye!")
            break

        if user_input.lower() in ["help", "?"]:
            display_help()
            continue

        response = get_response(user_input)
        format_bot_reply(response)

if __name__ == "__main__":
    run_chatbot()