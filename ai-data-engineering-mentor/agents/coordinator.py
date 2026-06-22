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