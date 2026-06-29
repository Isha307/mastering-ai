def get_router_prompt():
    return """
You are a routing agent.

Classify the user's question into exactly one category:

- sql
- beam
- interview
- general

Examples:

Question: Optimize this SQL query
Answer: sql

Question: Explain Apache Beam side inputs
Answer: beam

Question: Conduct a mock Data Engineering interview
Answer: interview

Question: What is data engineering?
Answer: general

Rules:
- Return ONLY the category name.
- Do not explain your answer.
- Do not return any extra text.
"""

def parse_route(response_text: str) -> str:
    response_text = response_text.strip().lower()

    valid_routes = [
        "sql",
        "beam",
        "interview",
        "general"
    ]

    if response_text in valid_routes:
        return response_text

    return "general"