# Email Drafting Agent

A multi-agent AI application built with CrewAI that helps users draft polished, professional emails from a short prompt. The system separates the work into two stages:

1. An analyst agent studies the email request, extracts the intent, and produces a structured brief.
2. A writer agent turns that brief into a concise, professional email.

The project is designed to be easy to run from the command line, with optional interactive prompts and direct argument-based execution.

---

## Overview

This project demonstrates a lightweight multi-agent workflow using CrewAI and OpenAI models. It is useful for:

- drafting follow-up emails
- creating outreach messages
- writing polite customer support emails
- generating professional communication from a simple description

The current implementation focuses on producing a final email with:

- a suggested subject line
- a professional greeting
- a concise body
- closing remarks and sender signature

---

## Features

- Multi-agent workflow with distinct analyst and writer roles
- Structured briefing before drafting the final output
- Configurable tone and recipient settings
- Interactive CLI prompts with defaults
- Command-line arguments for non-interactive use
- Environment-based OpenAI configuration
- Memory enabled in the Crew workflow

---

## Project Structure

```text
email-drafting-agent/
├── agent.py             # CLI entry point and prompt handling
├── agents.py            # Agent definitions
├── config.py            # LLM configuration and valid tone options
├── crew.py              # Crew assembly and task orchestration
├── tasks.py             # Task definitions for analysis and writing
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables for API access
├── README.md            # Project documentation
└── tests/               # Optional simple regression tests
```

---

## Requirements

Before running the project, make sure you have:

- Python 3.9 or newer
- An OpenAI API key
- Internet access to call the OpenAI API

---

## Installation

1. Open a terminal in the project folder.
2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root with the following values:

```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
```

### Environment variables

- `OPENAI_API_KEY`: Your secret API key from OpenAI.
- `OPENAI_MODEL`: The model name to use. The default is `gpt-4o-mini`.

> Replace the placeholder value with your real key before running the agent. If the key is missing, the script exits with a message.

---

## Usage

### 1) Interactive CLI mode

Run the project without arguments:

```bash
python agent.py
```

The program will prompt you for:

- email context
- tone
- recipient
- sender

Press Enter to accept the default values shown in square brackets.

### 2) Non-interactive CLI mode

You can also pass values directly as command-line arguments:

```bash
python agent.py \
  --context "Follow up on the proposal" \
  --tone "professional" \
  --recipient "HR Manager" \
  --sender "Mohit"
```

### 3) Example with a custom prompt

```bash
python agent.py --context "Request a meeting to discuss the new partnership opportunity" --tone "friendly" --recipient "Potential Client" --sender "Alex"
```

---

## Workflow

The workflow is sequential:

```text
User Input
   │
   ▼
Email Context Analyst
   │
   ▼
Structured Brief
   │
   ▼
Professional Email Writer
   │
   ▼
Final Email Output
```

### Agent roles

#### Email Context Analyst
This agent reviews the input request and creates a structured brief containing:

- purpose
- key points
- CTA (call to action)
- subject suggestion
- writing style

#### Professional Email Writer
This agent uses the structured brief to write a complete, polished email that fits the target tone and recipient.

---

## Code Overview

### [agent.py](agent.py)
This is the main executable script. It:

- parses command-line arguments
- prompts interactively if values are not passed
- builds the crew
- runs the crew and prints the final email

### [agents.py](agents.py)
Defines the two CrewAI agents:

- `email_context_analyst()`
- `email_writer()`

### [tasks.py](tasks.py)
Defines the tasks for the workflow:

- `analyze_email_task(...)`
- `write_email_task(...)`

These tasks tell the agents what information to gather and how to structure the final email.

### [crew.py](crew.py)
Assembles the agents and tasks into a Crew and runs them in sequence using `Process.sequential`.

### [config.py](config.py)
Contains:

- environment loading via `python-dotenv`
- model configuration
- the valid tone list used by the CLI

---

## Supported Tone Values

The system accepts these tones:

- `professional`
- `professional and friendly`
- `friendly`
- `formal`
- `casual`
- `persuasive`

If you enter an unknown tone, the script prints a warning and continues.

---

## Example Output

```text
Subject: Follow-up on Product Demo

Dear John,

Thank you for taking the time to attend our product demonstration last Tuesday. I appreciated the opportunity to discuss your goals and explore how our solution could support your team.

Please let me know if you would like to schedule a follow-up conversation next week.

Regards,

Mohit
```

---

## Running the Script

From the project directory:

```bash
python agent.py
```

If you want to skip the prompt flow and directly provide inputs:

```bash
python agent.py --context "Thanks for your time" --tone "professional" --recipient "Client" --sender "Alex"
```

---
