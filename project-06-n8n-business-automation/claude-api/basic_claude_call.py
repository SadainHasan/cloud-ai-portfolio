"""
basic_claude_call.py
--------------------
Simplest possible Claude API call.
Sends one question, prints the answer.
Run: python basic_claude_call.py
"""

import anthropic
import os

def ask_claude(question: str) -> str:
    """
    Send a single question to Claude and return the text response.
    
    Uses claude-haiku-4-5-20251001 — the most cost-efficient model.
    For reference only / study purposes, keep usage low.
    """
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    
    return message.content[0].text


if __name__ == "__main__":
    question = "Explain S3 lifecycle rules in exactly 3 bullet points."
    print(f"\nQuestion: {question}")
    print(f"\nClaude's answer:\n{'-'*40}")
    answer = ask_claude(question)
    print(answer)
    print(f"{'-'*40}\n")