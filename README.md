# BP Cheats

BP Cheats is an automated Linux command execution and documentation tool that converts natural language instructions from DOCX files into executable Linux commands, runs them in a controlled environment, and generates detailed reports with visual outputs.

## What It Does

This project automates the process of:
1. Reading natural language instructions from DOCX files
2. Converting those instructions into Linux terminal commands using an AI language model
3. Executing those commands in a sandboxed environment
4. Capturing the terminal output as images
5. Generating a comprehensive DOCX report with the original instructions, commands, descriptions, and visual outputs

It's particularly useful for:
- Automating repetitive Linux tasks described in documentation
- Creating visual records of command execution processes
- Converting procedural text instructions into executable workflows
- Educational purposes for learning Linux commands

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenRouter API key:
   - Open the `.env` file
   - Replace `your_openrouter_api_key_here` with your actual OpenRouter API key

## How It Works

The main automation workflow in `index.py` performs these steps:

1. **Clears the field directory** - Prepares a clean environment for command execution
2. **Reads DOCX instructions** - Extracts natural language instructions from DOCX files
3. **Generates Linux commands** - Uses an LLM to convert instructions into executable commands
4. **Executes commands** - Runs each command in the field directory with a delay between executions
5. **Captures outputs** - Generates PNG images of each command's terminal output
6. **Creates a report** - Produces a new DOCX file containing:
   - Original instructions
   - Each command with a human-readable description
   - Visual output of each command's execution

## Usage

### Complete Automation

Run the complete automated workflow:
```bash
python index.py
```

### Individual Components

#### Reading DOCX Files
Use the `read_docx_file` function from `util.py` to read the contents of DOCX files:

```python
from util import read_docx_file

content = read_docx_file("exprement number 3.docx")
print(content)
```

#### Using the LLM Function
Use the `ask_llm` function from `llm.py` to interact with the LLM:

```python
from llm import ask_llm

response = ask_llm(
    system_prompt="You are a helpful assistant.",
    user_message="What is the meaning of life?"
)
print(response)
```

#### Terminal Emulator
Use the `run_command_and_capture_output` function from `terminal_emulator.py` to run commands in the `/field` directory and generate PNG images of the output:

```python
from terminal_emulator import run_command_and_capture_output

output_path = run_command_and_capture_output("ls -la")
print(f"Output saved to: {output_path}")
```

## Project Structure

- `util.py`: Utility functions for reading DOCX files
- `llm.py`: Function to interact with the OpenRouter API
- `terminal_emulator.py`: Function to run commands and generate output PNGs
- `index.py`: Main orchestration script that ties everything together
- `test_util.py`: Test script for the DOCX reading function
- `test_llm.py`: Test script for the LLM function
- `test_terminal.py`: Test script for the terminal emulator
- `requirements.txt`: List of required Python packages
- `.env`: Environment variables (API keys, etc.)
- `field/`: Directory where commands are executed
- `output/`: Directory where command output PNGs and final reports are saved
- `data/`: Directory containing DOCX files (instructions)