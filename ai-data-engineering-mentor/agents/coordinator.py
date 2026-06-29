from agents.sql_agent import handle as sql_handle
from agents.beam_agent import handle as beam_handle
from agents.interview_agent import handle as interview_handle
## Agent Orchestration

def route_question(question: str) -> str:
    question = question.lower()

    if any(keyword in question for keyword in [
        "sql",
        "query",
        "join",
        "cte",
        "window function"
    ]):
        return "sql"

    if any(keyword in question for keyword in [
        "beam",
        "dataflow",
        "side input",
        "watermark",
        "trigger",
        "pcollection"
    ]):
        return "beam"

    if any(keyword in question for keyword in [
        "interview",
        "mock interview",
        "resume",
        "faang"
    ]):
        return "interview"

    return "general"

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