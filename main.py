import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"

with open("profile.txt", "r", encoding="utf-8") as f:
    PROFILE = f.read()

SYSTEM_PROMPT = f"""You are the personal assistant for Sriram J.
Answer ONLY using the PROFILE below.
- If the question is about Sriram and the answer is in the PROFILE, answer briefly.
- For anything else (general knowledge, coding help, news, opinions, or details
  not in the PROFILE), reply exactly: I don't know.
Never guess and never use outside knowledge.

PROFILE:
{PROFILE}
"""


def ask(question: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("Sriram's personal chatbot (type 'exit' to quit)")
    while True:
        q = input("You: ").strip()
        if q.lower() in {"exit", "quit"}:
            break
        if q:
            print("Bot:", ask(q))
