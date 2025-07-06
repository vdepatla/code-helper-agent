# Code Helper Agent

This project is an AI-powered code analysis and documentation tool built with [LangChain](https://python.langchain.com/), [LangGraph](https://github.com/langchain-ai/langgraph), and [OpenAI GPT-4](https://platform.openai.com/docs/models/gpt-4). It automates the process of understanding code, detecting its programming language, analyzing its functionality, and generating documentation.

## Features

- **Language Detection:** Identifies the programming language of a code snippet.
- **Functionality Analysis:** Summarizes what the code does and its main purpose.
- **Automated Documentation:** Generates documentation including a description, function details, and suggestions for improvement.

## How It Works

The agent uses a workflow graph with three main steps:
1. **detect_language:** Determines the programming language.
2. **analyze_functionality:** Explains the code's purpose.
3. **generate_documentation:** Produces structured documentation.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/code-helper-agent.git
   cd code-helper-agent
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv agent_env
   source agent_env/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your `.env` file:**
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Import and use the `code_helper` workflow in your Python code. Provide a `State` dictionary with at least the `code` key:

```python
from code_helper_agent import code_helper

state = {"code": "def add(a, b): return a + b"}
result = code_helper.invoke(state)
print(result["documentation"])
```

## File Structure

- `code_helper_agent.py` — Main workflow and logic.
- `.env` — Environment variables (not tracked by git).
- `agent_env/` — Virtual environment directory (not tracked by git).

## Notes

- Make sure your `.env` and `agent_env/` directories are listed in `.gitignore` to avoid committing sensitive data or virtual environment files.