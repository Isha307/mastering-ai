import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import json
from agents.coordinator import route_question
from agents.sql_agent import get_sql_system_prompt
from agents.beam_agent import get_beam_system_prompt
from agents.interview_agent import get_interview_system_prompt

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

agent_type = route_question(user_question)
agent_prompt = ""

if agent_type == "sql":
    agent_prompt = get_sql_system_prompt()
elif agent_type == "beam":
    agent_prompt = get_beam_system_prompt()
elif agent_type == "interview":
    agent_prompt = get_interview_system_prompt()
else:    
    agent_prompt = "You are a helpful and knowledgeable Data Engineering Mentor. Answer the user's question to the best of your ability."     

print(f"Selected Agent: {agent_type}")
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