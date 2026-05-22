"""
claude_study_assistant.py
--------------------------
Command-line AI study assistant powered by the Anthropic Claude API.
Specialised for AWS SAA-C03 exam preparation and cloud computing questions.

Usage: python claude_study_assistant.py
Type your question and press Enter. Type 'quit' to exit.
Type 'help' to see example questions.

Portfolio project: Cloud + AI Automation — Hasan
GitHub: https://github.com/SadainHasan/cloud-ai-portfolio
"""

import anthropic
import os
import sys
from datetime import datetime

# System prompt — this shapes Claude's persona and expertise
SYSTEM_PROMPT = """You are AWS Maya, a specialist AWS SAA-C03 exam coach and cloud computing tutor.

Your student is Hasan — a former VP-level IT leader from Bangladesh with 13 years of banking 
technology experience, now studying for the AWS Solutions Architect Associate exam.

When answering questions:
1. Give clear, exam-focused answers. Flag any SAA-C03 exam traps explicitly.
2. Connect concepts to real-world scenarios, especially banking or financial services where relevant.
3. Use analogies that relate to Hasan's banking IT background when helpful.
4. End every answer with ONE exam tip in this format: EXAM TIP: [tip text]
5. Keep answers under 250 words unless a longer answer is clearly needed.
6. If asked about cost, always mention the most cost-efficient AWS option first.

You are strict, practical, and exam-focused. No fluff."""


def print_banner():
    """Print the study assistant welcome banner."""
    print("\n" + "="*60)
    print("  AWS STUDY ASSISTANT — Powered by Claude API")
    print("  Cloud + AI Automation Portfolio — Hasan")
    print("  Model: claude-haiku-4-5-20251001")
    print("="*60)
    print("  Type your question and press Enter.")
    print("  Type 'help' for example questions.")
    print("  Type 'quit' to exit.")
    print("="*60 + "\n")


def print_help():
    """Print example questions."""
    examples = [
        "What is the difference between S3 Standard and S3 Standard-IA?",
        "When should I use RDS Multi-AZ vs Read Replicas?",
        "Explain VPC subnets — public vs private",
        "What is the maximum size of an S3 object?",
        "When does Lambda cold start occur and how do I prevent it?",
        "What is the difference between Security Groups and NACLs?",
    ]
    print("\n--- Example questions ---")
    for i, q in enumerate(examples, 1):
        print(f"  {i}. {q}")
    print()


def ask_claude(client: anthropic.Anthropic, question: str) -> str:
    """
    Send a question to Claude with the study assistant system prompt.
    Returns the response text.
    """
    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        return message.content[0].text
    except anthropic.APIConnectionError:
        return "ERROR: Could not connect to Anthropic API. Check your internet connection."
    except anthropic.AuthenticationError:
        return "ERROR: Invalid API key. Check your ANTHROPIC_API_KEY environment variable."
    except anthropic.RateLimitError:
        return "ERROR: Rate limit hit. Wait 60 seconds and try again."
    except anthropic.APIError as e:
        return f"ERROR: API error — {str(e)}"


def save_session_log(session_questions: list, session_start: datetime):
    """Save this study session to a log file."""
    log_filename = f"session-log-{session_start.strftime('%Y%m%d-%H%M')}.txt"
    with open(log_filename, "w", encoding="utf-8") as f:
        f.write(f"AWS Study Session — {session_start.strftime('%Y-%m-%d %H:%M')}\n")
        f.write("="*60 + "\n\n")
        for i, (q, a) in enumerate(session_questions, 1):
            f.write(f"Q{i}: {q}\n")
            f.write(f"A{i}: {a}\n")
            f.write("-"*40 + "\n\n")
    print(f"\n✅ Session log saved: {log_filename}")


def main():
    """Main study assistant loop."""
    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("\nERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("Run: set ANTHROPIC_API_KEY=sk-ant-api03-your-key-here")
        print("Then restart this script.\n")
        sys.exit(1)
    
    # Initialise client
    client = anthropic.Anthropic(api_key=api_key)
    
    print_banner()
    
    session_questions = []
    session_start = datetime.now()
    question_count = 0
    
    while True:
        try:
            user_input = input("Ask Claude ▶  ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        
        if not user_input:
            continue
        
        if user_input.lower() in ("quit", "exit", "q"):
            break
        
        if user_input.lower() == "help":
            print_help()
            continue
        
        question_count += 1
        print(f"\n[Question {question_count} — {datetime.now().strftime('%H:%M')}]")
        print("Thinking...\n")
        
        answer = ask_claude(client, user_input)
        print(answer)
        print()
        
        session_questions.append((user_input, answer))
    
    # End of session
    print(f"\n{'='*60}")
    print(f"  Session ended. Questions asked: {question_count}")
    
    if session_questions:
        save_log = input("  Save session log? (y/n): ").strip().lower()
        if save_log == "y":
            save_session_log(session_questions, session_start)
    
    print("  Good session, Hasan. Keep building.\n")


if __name__ == "__main__":
    main()