# AI Agent in Python

A small AI agent project built while following the Boot.dev AI Agent course. The goal of this project was to better understand how AI agents work behind the scenes — how they decide what to do, call the right tools, and loop until they have a final answer. Python acts as the glue between the user's prompt and the Gemini API, handling everything from function calling to file I/O.

The agent takes a user prompt from the terminal, talks to Google's Gemini model, and can autonomously read files, list directories, run Python scripts, and write files — all within a sandboxed working directory. It keeps going back and forth with the model until it has a proper response or hits the iteration limit.

---

## Features

* Accepts user prompts directly from the terminal via `argparse`
* Connects to Google's Gemini 2.5 Flash model for reasoning
* Supports tool/function calling — the model can decide which tools to use on its own
* Built-in tools: list files, read file contents, execute Python scripts, and write files
* Sandboxed file access — all operations are restricted to a permitted working directory
* Agentic loop with a configurable max iteration limit
* Verbose mode for debugging (shows token usage, function calls, and results)
* Comes with a sample calculator app the agent can interact with
* Includes unit-style tests for each tool function

---

## Tech Stack

* Python 3.13
* Google Gemini API (`google-genai`)
* Function Calling / Tool Use
* `subprocess` for running Python files
* `argparse` for CLI interaction
* `python-dotenv` for environment variable management
* `uv` for dependency management
* Git & GitHub

---

## Skills Highlighted

This project helped me improve and demonstrate skills in:

* Python scripting and project structuring
* Working with LLM APIs and function calling
* Designing agentic loops (prompt → model → tool → model → response)
* Building modular tool functions with proper schemas
* Input validation and sandboxing (preventing directory traversal)
* Subprocess management and capturing stdout/stderr
* Error handling and edge case coverage
* Environment variable management with `.env` files
* Writing tests to verify tool behavior
* CLI design with `argparse`
* Git version control

---

## Project Structure

```
.
├── main.py                    # Entry point — runs the agentic loop
├── prompt.py                  # System prompt for the AI agent
├── call_function.py           # Maps function calls to actual Python functions
├── functions/
│   ├── get_files_info.py      # Tool: list files in a directory
│   ├── get_file_content.py    # Tool: read file contents
│   ├── run_python_file.py     # Tool: execute a Python script
│   └── write_file.py          # Tool: write content to a file
├── calculator/                # Sample project the agent can work with
│   ├── main.py
│   ├── pkg/
│   ├── tests.py
│   └── lorem.txt
├── test_get_file_content.py   # Tests for file reading tool
├── test_get_files_info.py     # Tests for directory listing tool
├── test_run_python_file.py    # Tests for script execution tool
├── test_write_file.py         # Tests for file writing tool
├── pyproject.toml             # Project metadata and dependencies
├── .env                       # API key (not committed)
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai_agent_project
```

### 2. Set up the environment

This project uses `uv` for dependency management. If you don't have it installed:

```bash
pip install uv
```

Then sync the dependencies:

```bash
uv sync
```

Or if you prefer using pip directly:

```bash
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

### 3. Add your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the agent

```bash
python main.py "What files are in the calculator project?"
```

With verbose output:

```bash
python main.py "Run the calculator tests and fix any issues" --verbose
```

---

## How It Works

1. You pass a prompt through the terminal
2. The agent sends it to Gemini along with the available tool schemas
3. Gemini decides whether to respond directly or call a tool
4. If it calls a tool (e.g., `get_files_info`), the agent executes it locally and sends the result back
5. This loop continues until Gemini gives a final text response or the max iterations (20) are reached

The interesting part is that the model figures out on its own which tools to call and in what order — you just describe what you want and it handles the rest.

---

## What I Learned

Building this project gave me a much better understanding of how AI agents actually work under the hood. It's one thing to use ChatGPT, but it's a completely different experience to build the loop yourself — watching the model decide to list files, read code, run tests, and then summarize the results all on its own.

I also got hands-on with function calling, which was probably the most interesting part. Defining tool schemas, handling the back-and-forth between the model and the tools, and making sure everything stays sandboxed taught me a lot about how real-world AI agents are built.

---

## Future Improvements

* Add conversation memory and context persistence
* Support more tools (web search, database queries, etc.)
* Add a web-based interface
* Implement better error recovery when the model hallucinates tool calls
* Add streaming support for real-time responses
* Deploy as a CLI tool via PyPI

---

## Author

Made by **Nakul** while learning AI Engineering and Python development.
