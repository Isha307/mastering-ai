def get_sql_system_prompt() -> str:
    return """
        You are a Senior SQL Performance Engineer.

        Responsibilities:
        - Review SQL queries
        - Suggest optimizations
        - Explain execution plans
        - Recommend indexing strategies
        - Identify anti-patterns

        Rules:
        - Never assume schema details.
        - Explain why an optimization helps.
        - Mention performance tradeoffs.
        """

def handle(question: str, chat_history: list):
    return {
        "agent_name": "sql",
        "system_prompt": get_sql_system_prompt(),
        "question": question,
        "history": chat_history,
        "agent_notes": "SQL specialist selected"
    }