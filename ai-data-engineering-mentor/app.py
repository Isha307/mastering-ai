import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import json
from agents.coordinator import get_agent_response

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

user_question = input("Ask your Data Engineering Mentor: ")

if user_question.strip().lower() == "/reset":
    save_chat_history([])
    print("Conversation history cleared.")
    exit()

agent_data = get_agent_response(
    user_question,
    chat_history
)

print(f"Selected Agent: {agent_data['agent_name']}")
agent_prompt = agent_data["system_prompt"]
MAX_HISTORY_MESSAGES = 10
recent_history = chat_history[-MAX_HISTORY_MESSAGES:]

print(f"Loaded {len(chat_history)} previous chat messages from chat_history.json")
base_context = load_system_context()
system_context = f"""
{base_context}

{agent_prompt}
"""

messages = [
    {
        "role": "system",
        "content": system_context,
    }
]

messages.extend(recent_history)

messages.append(
    {
        "role": "user",
        "content": user_question
    }
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=messages
)

assistant_response = response.choices[0].message.content

chat_history.append(
    {
        "role": "user",
        "content": user_question
    }
)

chat_history.append(
    {
        "role": "assistant",
        "content": assistant_response
    }
)


save_chat_history(chat_history)

print("\n=== MENTOR RESPONSE ===\n")
print(assistant_response)