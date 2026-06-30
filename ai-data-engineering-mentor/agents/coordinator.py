from agents.sql_agent import handle as sql_handle
from agents.beam_agent import handle as beam_handle
from agents.interview_agent import handle as interview_handle
from agents.router_agent import route_with_llm
## Agent Orchestration

def route_question(question: str) -> str:
    return route_with_llm(question)

def get_agent_response(question: str, chat_history: list):
    agent_type = route_question(question)

    if agent_type == "sql":
        return sql_handle(question, chat_history)

    elif agent_type == "beam":
        return beam_handle(question, chat_history)

    elif agent_type == "interview":
        return interview_handle(question, chat_history)

    return {
        "agent_name": "general",
        "system_prompt": "You are a helpful Data Engineering Mentor.",
        "question": question,
        "history": chat_history
    }