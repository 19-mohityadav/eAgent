import argparse
import os
import sys

from dotenv import load_dotenv

from config import VALID_TONES
from crew import build_email_crew

load_dotenv()

DEFAULT_CONTEXT = "Follow up on our product demo from last Tuesday."
DEFAULT_TONE = "professional and friendly"
DEFAULT_RECIPIENT = "Potential Client"
DEFAULT_SENDER = "Your Name"

if not os.getenv("OPENAI_API_KEY"):
    print("OPENAI_API_KEY missing in .env")
    sys.exit(1)


def collect_user_inputs(args=None):
    print("Email Drafting Agent")
    print("Press Enter to use the default value shown in brackets.\n")

    prompt_args = args or argparse.Namespace(
        context=None,
        tone=None,
        recipient=None,
        sender=None,
    )

    values = {
        "context": (
            prompt_args.context
            if getattr(prompt_args, "context", None) is not None
            else input(f"Email context [{DEFAULT_CONTEXT}]: ").strip() or DEFAULT_CONTEXT
        ),
        "tone": (
            prompt_args.tone
            if getattr(prompt_args, "tone", None) is not None
            else input(f"Tone [{DEFAULT_TONE}]: ").strip() or DEFAULT_TONE
        ),
        "recipient": (
            prompt_args.recipient
            if getattr(prompt_args, "recipient", None) is not None
            else input(f"Recipient [{DEFAULT_RECIPIENT}]: ").strip() or DEFAULT_RECIPIENT
        ),
        "sender": (
            prompt_args.sender
            if getattr(prompt_args, "sender", None) is not None
            else input(f"Sender [{DEFAULT_SENDER}]: ").strip() or DEFAULT_SENDER
        ),
    }

    if values["tone"].lower() not in [t.lower() for t in VALID_TONES]:
        print("Warning: Unknown tone. Continuing...\n")

    return values


def main():
    parser = argparse.ArgumentParser(
        description="CrewAI Email Drafting Agent"
    )

    parser.add_argument(
        "--context",
        default=None,
    )

    parser.add_argument(
        "--tone",
        default=None,
    )

    parser.add_argument(
        "--recipient",
        default=None,
    )

    parser.add_argument(
        "--sender",
        default=None,
    )

    args = parser.parse_args()
    user_inputs = collect_user_inputs(args)

    crew = build_email_crew(
        user_inputs["context"],
        user_inputs["tone"],
        user_inputs["recipient"],
        user_inputs["sender"],
    )

    print("\nGenerating your email...\n")
    result = crew.kickoff()

    print("\n")
    print("=" * 70)
    print("EMAIL")
    print("=" * 70)
    print(result)
    print("=" * 70)


if __name__ == "__main__":
    main()