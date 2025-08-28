# BP Cheats

## What Does It Do?

This is a cheat for BladePlay to be lazy and automate his college assignments. It takes a docx file of the assignment and solves it producing a docx with "proof" that he did it.

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
   - Create the `.env` file
   - Put `OPENROUTER_API_KEY=your_openrouter_api_key_here` in the `.env` file

## How It Works (only nerds read this)

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

Put the assignment docx file into `/data`

Run the complete automated workflow:
```bash
python index.py
```
