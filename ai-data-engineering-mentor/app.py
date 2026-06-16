import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def load_system_context():
    prompt = Path("prompt.md").read_text(encoding="utf-8")
    skills = Path("skills.md").read_text(encoding="utf-8")
    precision = Path("precision.md").read_text(encoding="utf-8")
    memory = Path("memory.md").read_text(encoding="utf-8")

    return f"""
{prompt}

{skills}

{precision}

{memory}
"""

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
system_context = load_system_context()

user_question = input("Ask your Data Engineering Mentor: ")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": system_context,
        },
        {
            "role": "user",
            "content": user_question,
        },
    ],
)

print("\n=== MENTOR RESPONSE ===\n")
print(response.choices[0].message.content)