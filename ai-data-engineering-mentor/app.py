import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import json
from pathlib import Path
from agents.coordinator import route_question

load_dotenv()


def load_chat_history():
    history_file = Path("chat_history.json")
    if history_file.exists():
        with open(history_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_chat_history(chat_history):
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=4)

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
chat_history = load_chat_history()

MAX_HISTORY_MESSAGES = 10
recent_history = chat_history[-MAX_HISTORY_MESSAGES:]

print(f"Loaded {len(chat_history)} previous chat messages from chat_history.json")
system_context = load_system_context()

user_question = input("Ask your Data Engineering Mentor: ")

if user_question.strip().lower() == "/reset":
    save_chat_history([])
    print("Conversation history cleared.")
    exit()

agent_type = route_question(user_question)
print(f"\nSelected Agent: {agent_type}\n")

chat_history.append({"role": "user", "content": user_question})
save_chat_history(chat_history)

messages = [
    {
        "role": "system",
        "content": system_context,
    }
]

messages.extend(recent_history)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=messages
)

assistant_response = response.choices[0].message.content

chat_history.append(
    {
        "role": "assistant",
        "content": assistant_response
    }
)

save_chat_history(chat_history)

print("\n=== MENTOR RESPONSE ===\n")
print(assistant_response)