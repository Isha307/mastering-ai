# AI Data Engineering Mentor

An AI-powered Data Engineering Mentor built using a context-engineering approach.

Instead of placing all instructions inside Python code, this project separates the AI's behavior into modular files:

* `prompt.md` → Identity
* `skills.md` → Capabilities
* `precision.md` → Response quality rules
* `memory.md` → User preferences and context

This structure makes the assistant easier to maintain, extend, and customize.

---

## Features

* Data Engineering mentoring
* SQL query reviews
* Apache Beam guidance
* Spark guidance
* Data modeling assistance
* Interview preparation support
* Personalized responses using memory

---

## Project Structure

```text
ai-data-engineering-mentor/
│
├── prompt.md
├── skills.md
├── precision.md
├── memory.md
├── .env
├── app.py
├── requirements.txt
└── README.md
```

### prompt.md

Defines the AI's identity and behavior.

Example:

```md
You are a Senior Staff Data Engineer and Mentor.
```

### skills.md

Defines what the AI can do.

Examples:

* SQL Optimization
* Apache Beam Development
* Spark Engineering
* Data Modeling
* Interview Coaching

### precision.md

Defines response quality standards.

Examples:

* Never assume schema names.
* Ask clarifying questions when information is missing.
* Explain tradeoffs for design decisions.

### memory.md

Stores user preferences and long-term context.

Example:

```md
Preferred Technologies:
- Apache Beam
- GCP
- BigQuery
```

---

## How It Works

The application loads all context files and combines them into a single system prompt.

```text
prompt.md
      +
skills.md
      +
precision.md
      +
memory.md
      ↓
System Context
      ↓
LLM
      ↓
Response
```

This pattern is known as Context Engineering.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ai-data-engineering-mentor
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key_here
```

For Groq users:

```env
OPENAI_API_KEY=gsk_xxxxxxxxxxxxxxxxx
```

---

## Running the Application

```bash
python app.py
```

Example:

```text
Ask your Data Engineering Mentor:
What are Apache Beam side inputs?
```

Output:

```text
Side inputs in Apache Beam allow...
```

---

## Tech Stack

* Python
* Groq API
* Llama 3.1
* python-dotenv
* Markdown-based Context Engineering

---

## Key Takeaway

The primary goal of this project is to learn how modern AI applications are built using structured context files rather than large hardcoded prompts. This approach improves maintainability, scalability, and experimentation while keeping the application simple and easy to understand.
