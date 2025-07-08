# Code Helper Agent

This project is an AI-powered code analysis and documentation tool built with [LangChain](https://python.langchain.com/), [LangGraph](https://github.com/langchain-ai/langgraph), and [OpenAI GPT-4](https://platform.openai.com/docs/models/gpt-4). It automates the process of understanding code, detecting its programming language, analyzing its functionality, and generating documentation.

![Code Helper Agent Screenshot](../assets/code_helper_agent_screenshot.png)

## Features

- **Language Detection:** Identifies the programming language of a code snippet.
- **Functionality Analysis:** Summarizes what the code does and its main purpose.
- **Automated Documentation:** Generates documentation including a description, function details, and suggestions for improvement.
- **Gradio UI:** Provides a simple web interface for interactive code analysis.

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

### Python API

Import and use the `code_helper` workflow in your Python code. Provide a `State` dictionary with at least the `code` key:

```python
from code_helper_agent import code_helper

state = {"code": "def add(a, b): return a + b"}
result = code_helper.invoke(state)
print(result["documentation"])
```

### Gradio UI

A Gradio web interface is available for interactive use.

#### To run the Gradio server locally:

1. Make sure Gradio is installed (it should be in `requirements.txt`). If not, install it:
   ```sh
   pip install gradio
   ```

2. Run the Gradio app (replace `gradio_app.py` with your actual Gradio UI file if different):
   ```sh
   python gradio_app.py
   ```

3. Open the provided local URL in your browser (usually `http://127.0.0.1:7860/`).

#### Example Gradio UI usage

- Paste your code snippet into the input box.
- Click the "Analyze" button.
- View the detected language, functionality summary, and generated documentation in the output area.

## File Structure

- `code_helper_agent.py` — Main workflow and logic.
- `gradio_app.py` — Gradio UI for interactive code analysis.
- `.env` — Environment variables (not tracked by git).
- `agent_env/` — Virtual environment directory (not tracked by git).

## .gitignore

Make sure your `.env` and `agent_env/` directories are listed in `.gitignore` to avoid committing sensitive data or virtual environment files:

```
agent_env/
.env
```

## Notes

- Do not commit your `.env` file or virtual environment directory.
- The Gradio UI makes it easy to use the agent without writing code.

