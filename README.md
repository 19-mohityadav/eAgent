# 📧 Email Drafting Agent

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Framework-green)](https://crewai.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/19-mohityadav/eAgent)

A lightweight, intelligent multi-agent email drafting system built with **CrewAI** that transforms brief, informal prompts into polished, professional emails. The system leverages a two-stage agent workflow to analyze intent and generate contextually appropriate correspondence.

---

## 📋 Overview

### The Problem

Writing professional emails is time-consuming. Crafting the right tone, structure, and language for different recipients—clients, managers, partners—requires context-switching and mental effort. Most email assistants offer generic templates or require extensive prompting to capture the right message.

### The Solution

**eAgent** uses a multi-agent orchestration approach where:

1. **An analyst agent** deconstructs your email intent, extracts key messaging, and structures a professional brief
2. **A writer agent** transforms that brief into a complete, polished email with subject line, greeting, body, and signature

This separation of concerns produces better emails because:
- **Structured analysis** ensures no context is lost
- **Focused writing** concentrates on tone and language without re-analyzing intent
- **Reproducibility** allows for iterative refinement of either stage independently
- **Agent specialization** lets each agent excel at its specific role

### Why CrewAI?

CrewAI provides a declarative, task-oriented framework for building multi-agent workflows. Unlike single-prompt systems, CrewAI enables:
- Clear role definitions with structured prompts
- Sequential task orchestration with context passing
- Built-in memory and tool integration
- Human-readable agent communication

### Real-World Use Cases

- **Follow-up emails** after meetings or presentations
- **Outreach campaigns** to potential clients or collaborators
- **Customer support** responses to inquiries
- **Professional communication** for HR, recruitment, or management
- **Networking emails** and connection requests
- **Status updates** and progress reports
- **Apology or clarification** emails requiring careful tone

---

## ✨ Features

- **Multi-agent workflow** with specialized analyst and writer roles
- **Structured briefing** ensures context is preserved and organized before writing
- **Configurable tone** selection from six professional tone options
- **Interactive CLI** with sensible defaults for fast execution
- **Non-interactive mode** via command-line arguments for automation and scripting
- **Environment-based configuration** for secure API key management
- **Session memory** enabled across the crew workflow for consistent context
- **Fast iteration** using OpenAI's `gpt-4o-mini` model for cost-effective processing
- **Production-ready** error handling with API key validation

---

## 🏗️ Architecture

### System Diagram

```
┌─────────────────────────────────────┐
│                                     │
│       Email Drafting Agent          │
│                                     │
└─────────────────────────────────────┘
                  │
                  │ User Input
                  │ (context, tone, recipient, sender)
                  ▼
        ┌─────────────────────┐
        │   Agent.py (CLI)    │
        │  Parse Arguments    │
        │ Collect Prompts     │
        └─────────────────────┘
                  │
                  ▼
        ┌─────────────────────────────┐
        │  Crew Manager (crew.py)     │
        │  Orchestrate Sequential     │
        │  Workflow with Memory       │
        └─────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   ┌──────────────┐  ┌──────────────┐
   │   Analyst    │  │    Writer    │
   │   Agent      │  │    Agent     │
   └──────────────┘  └──────────────┘
        │                   │
        │ Task 1            │ Task 2
        │                   │
        ▼                   ▼
   ┌──────────────┐  ┌──────────────┐
   │ Analyze      │  │ Write Email  │
   │ Intent &     │  │ Using Brief  │
   │ Structure    │  │ as Context   │
   │ Brief        │  │              │
   └──────────────┘  └──────────────┘
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │  Shared Memory       │
        │  (Brief + Context)   │
        └──────────────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │  Final Email Output  │
        │  (with subject line) │
        └──────────────────────┘
```

### Component Responsibilities

#### **User Input (agent.py)**
- Parses command-line arguments or prompts user interactively
- Collects: email context, tone, recipient name, and sender name
- Validates tone against supported options
- Passes inputs to the Crew Manager

#### **Crew Manager (crew.py)**
- Instantiates the analyst and writer agents
- Creates tasks with proper context and dependencies
- Assembles the crew with sequential processing and memory enabled
- Orchestrates the workflow execution

#### **Email Context Analyst (agents.py + tasks.py)**
- **Role**: Email Context Analyst
- **Goal**: Understand the email request and create a structured brief
- **Input**: User's raw email context, recipient type, desired tone
- **Output**: Structured brief containing purpose, key points, CTA, subject suggestion, and writing style

#### **Professional Email Writer (agents.py + tasks.py)**
- **Role**: Professional Email Writer
- **Goal**: Write concise and professional emails
- **Input**: Analyst's structured brief (via crew memory)
- **Output**: Complete, ready-to-send email with proper formatting (under 200 words)

#### **Configuration (config.py)**
- Loads environment variables securely via `python-dotenv`
- Initializes the LangChain OpenAI LLM client with the specified model and temperature
- Maintains valid tone options for input validation

---

## 📁 Project Structure

```
eAgent/
├── agent.py              # CLI entry point and input collection
├── agents.py             # Agent definitions (analyst, writer)
├── config.py             # LLM configuration and tone options
├── crew.py               # Crew assembly and orchestration
├── tasks.py              # Task definitions for agents
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (API key)
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

### File Descriptions

| File | Purpose |
|------|---------|
| `agent.py` | Main entry point. Handles CLI argument parsing, interactive prompts, and crew initialization. Validates that `OPENAI_API_KEY` is set before running. |
| `agents.py` | Defines the two CrewAI agents using their role, goal, and backstory. Both agents use the shared LLM configured in `config.py`. |
| `tasks.py` | Defines the two sequential tasks: email analysis (structured brief generation) and email writing (final output). Task 2 depends on Task 1's output. |
| `crew.py` | Assembles agents and tasks into a Crew with sequential processing (`Process.sequential`) and memory enabled (`memory=True`). |
| `config.py` | Loads API key and model name from `.env`, instantiates the LangChain OpenAI LLM client, and maintains the list of valid tones. |
| `requirements.txt` | Python package dependencies: CrewAI, LangChain OpenAI, OpenAI SDK, and python-dotenv. |
| `.env` | User-created file containing `OPENAI_API_KEY` and optionally `OPENAI_MODEL`. |

---

## 🛠️ Technologies Used

| Technology | Role | Why Chosen |
|-----------|------|-----------|
| **Python 3.9+** | Core language | Industry standard for AI/ML work; simplicity for multi-agent orchestration |
| **CrewAI** | Agent framework | Declarative, high-level API for multi-agent workflows; excellent context passing between tasks |
| **LangChain OpenAI** | LLM integration | Unified interface for OpenAI API; seamless integration with CrewAI |
| **OpenAI API** | Language model backbone | State-of-the-art reasoning and writing; `gpt-4o-mini` balances quality and cost |
| **python-dotenv** | Environment management | Secure API key management without hardcoding; follows 12-factor app principles |
| **argparse** | CLI framework | Built-in Python module; lightweight and sufficient for argument parsing |

---

## 🤖 Multi-Agent Workflow

### Agent 1: Email Context Analyst

| Aspect | Details |
|--------|---------|
| **Role** | Email Context Analyst |
| **Goal** | Understand the email request and create a structured brief |
| **Backstory** | You analyze email requests, identify objectives, extract important information, and prepare instructions for the email writer. |
| **Inputs** | User's email context, recipient type, desired tone |
| **Outputs** | Structured brief with: Purpose, Key Points, CTA, Subject Suggestion, Writing Style |
| **Responsibilities** | Deconstruct user intent; extract messaging objectives; format findings for the writer agent |
| **Communication** | One-way output via CrewAI's task context mechanism; output becomes input for Task 2 |
| **Why It Exists** | Ensures intent is properly understood before writing, reducing revisions and improving clarity |

### Agent 2: Professional Email Writer

| Aspect | Details |
|--------|---------|
| **Role** | Professional Email Writer |
| **Goal** | Write concise and professional emails |
| **Backstory** | You are an experienced business copywriter capable of writing polished emails that achieve their intended goal. |
| **Inputs** | Analyst's structured brief (via crew memory), recipient name, tone, sender name |
| **Outputs** | Complete professional email with subject line, greeting, body, and signature |
| **Responsibilities** | Transform brief into polished prose; apply tone consistently; maintain professionalism; stay under 200 words |
| **Communication** | Receives analyst output via `context=[analysis_task]` parameter in task definition |
| **Why It Exists** | Separates the concern of writing from analysis; allows focused optimization of language and formatting |

### Task Execution Flow

1. **Task 1: Analyze Email Request**
   - Agent: Email Context Analyst
   - Input: User context, recipient, tone
   - Process: Deconstruct intent, extract key points, structure messaging
   - Output: Structured brief

2. **Task 2: Write Professional Email**
   - Agent: Professional Email Writer
   - Input: Analyst's brief (passed via `context=[analysis_task]`), recipient, tone, sender
   - Process: Compose email adhering to tone, structure, and word limit
   - Output: Final email with subject and signature

Both tasks execute sequentially using `Process.sequential`, ensuring the analyst completes before the writer begins.

---

## 📦 Installation

### Prerequisites

- **Python 3.9 or newer**
- **OpenAI API key** (from https://platform.openai.com/account/api-keys)
- **Internet connection** for API calls

### Step 1: Clone the Repository

```bash
git clone https://github.com/19-mohityadav/eAgent.git
cd eAgent
```

### Step 2: Create a Virtual Environment

Using `venv` (recommended):

```bash
python -m venv .venv
```

Activate the virtual environment:

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
.\.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
touch .env
```

Add the following to `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

**Important:**
- Replace `your_openai_api_key_here` with your actual OpenAI API key
- The `OPENAI_MODEL` defaults to `gpt-4o-mini`; you can change it to `gpt-4`, `gpt-3.5-turbo`, etc.
- **Never commit `.env` to version control**. It's included in `.gitignore`.

### Step 5: Verify Installation

Test that everything is set up correctly:

```bash
python agent.py --context "Test email" --tone "professional" --recipient "Test" --sender "Test"
```

If successful, you'll see the generated email output.

---

## ⚙️ Configuration

### Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `OPENAI_API_KEY` | *required* | Your secret OpenAI API key. Without this, the script exits with an error. |
| `OPENAI_MODEL` | `gpt-4o-mini` | The OpenAI model to use. Options: `gpt-4`, `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo`, etc. |

### Model Temperature

The system uses a fixed **temperature of 0.3** (set in `config.py`), which provides:
- **Consistency**: Low temperature makes outputs deterministic and predictable
- **Professionalism**: Reduces creative tangents inappropriate for business emails
- **Reliability**: Minimizes hallucinations and off-topic content

If you need higher creativity (e.g., for creative copy), you can modify `config.py`:

```python
llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0.7,  # Increase for more creativity
)
```

### Supported Tones

The system accepts these tone options:

- `professional` — Standard business tone
- `professional and friendly` — Warm but formal
- `friendly` — Casual and approachable
- `formal` — Highly ceremonial and reserved
- `casual` — Relaxed and conversational
- `persuasive` — Persuasive and sales-oriented

If you provide an unsupported tone, the system prints a warning but continues execution.

---

## 💻 Usage

### Mode 1: Interactive CLI (Recommended for First-Time Use)

Run without arguments to be prompted for each input:

```bash
python agent.py
```

**Output:**
```
Email Drafting Agent
Press Enter to use the default value shown in brackets.

Email context [Follow up on our product demo from last Tuesday.]: Your context here
Tone [professional and friendly]: professional
Recipient [Potential Client]: John Smith
Sender [Your Name]: Alice Chen

Generating your email...

======================================================================
EMAIL
======================================================================
Subject: Follow-up on Product Demo

Dear John,

Thank you for attending our product demonstration. I appreciated the opportunity to discuss your goals and explore how our solution could support your team.

I would love to schedule a follow-up call next week to address any questions.

Best regards,

Alice Chen
======================================================================
```

Press Enter at any prompt to use the default value shown in brackets.

### Mode 2: Non-Interactive CLI (For Automation)

Pass all arguments directly:

```bash
python agent.py \
  --context "Follow up on the proposal" \
  --tone "professional" \
  --recipient "HR Manager" \
  --sender "Mohit"
```

### Mode 3: Scripting & Integration

Use in shell scripts or automation pipelines:

```bash
#!/bin/bash

CONTEXT="Request meeting to discuss partnership"
TONE="friendly"
RECIPIENT="Potential Partner"
SENDER="Alex"

python agent.py \
  --context "$CONTEXT" \
  --tone "$TONE" \
  --recipient "$RECIPIENT" \
  --sender "$SENDER"
```

### Example Commands

#### Example 1: Sales Outreach

```bash
python agent.py \
  --context "Introducing our new analytics platform that reduces reporting time by 40%" \
  --tone "persuasive" \
  --recipient "VP of Operations" \
  --sender "Sarah"
```

#### Example 2: Customer Support

```bash
python agent.py \
  --context "Customer reported issue with login; we've fixed it and want to follow up" \
  --tone "professional and friendly" \
  --recipient "Customer" \
  --sender "Support Team"
```

#### Example 3: Networking

```bash
python agent.py \
  --context "Met at tech conference; want to connect and discuss collaboration" \
  --tone "friendly" \
  --recipient "Tech Lead from ConferenceX" \
  --sender "Jordan"
```

#### Example 4: Formal Notice

```bash
python agent.py \
  --context "Announce company restructuring with new reporting structure" \
  --tone "formal" \
  --recipient "All Staff" \
  --sender "CEO"
```

---

## 🔄 Task Flow & Execution

### Sequential Execution Model

eAgent uses CrewAI's **sequential processing** model, meaning tasks execute one after another, with each task having access to previous outputs:

```
┌──────────────┐
│ Task 1       │
│ Analyze      │
└──────┬───────┘
       │ Output (Brief)
       ▼
┌──────────────┐
│ Task 2       │
│ Write Email  │
│ (uses Brief) │
└──────┬───────┘
       │ Output (Final Email)
       ▼
    Display
```

### Detailed Execution Steps

1. **User Input Collection** (`agent.py`)
   - Parse command-line arguments or prompt interactively
   - Validate tone against supported options
   - Collect: `context`, `tone`, `recipient`, `sender`

2. **Crew Initialization** (`crew.py`)
   - Instantiate analyst and writer agents with LLM configuration
   - Create Task 1 (analyze) with user inputs
   - Create Task 2 (write) with dependency on Task 1 output
   - Assemble crew with `Process.sequential` and `memory=True`

3. **Task 1 Execution: Email Analysis** (`agents.py` + `tasks.py`)
   - **Agent**: Email Context Analyst
   - **Receives**: User context, recipient type, tone preference
   - **Produces**: Structured brief with purpose, key points, CTA, subject, style
   - **Duration**: ~2-5 seconds

4. **Task 2 Execution: Email Writing** (`agents.py` + `tasks.py`)
   - **Agent**: Professional Email Writer
   - **Receives**: Analyst's brief (via crew memory + `context` parameter)
   - **Constraints**: Under 200 words, specified tone, professional format
   - **Produces**: Complete email with subject, greeting, body, closure
   - **Duration**: ~3-8 seconds

5. **Output & Display** (`agent.py`)
   - Print formatted email output
   - Total execution time: ~5-15 seconds (depending on API latency)

### Memory & Context Passing

CrewAI's built-in memory system enables:
- **Long-term memory**: Crew remembers all previous task outputs
- **Context chaining**: Task 2 automatically receives Task 1's output via the `context=[analysis_task]` parameter
- **Consistency**: Both agents work with the same context throughout the workflow

---

## 🧩 Code Design

### Modularity & Separation of Concerns

The codebase is organized into five focused modules, each with a single responsibility:

#### **1. `agent.py` — CLI and User Interaction**
- **Responsibility**: Argument parsing, interactive prompts, input validation, script execution
- **Why modular**: Changes to CLI/UX don't affect agent logic or configuration
- **Key functions**:
  - `collect_user_inputs()`: Collects and validates user input
  - `main()`: Entry point and orchestration

#### **2. `agents.py` — Agent Definitions**
- **Responsibility**: Define agent roles, goals, and behavior
- **Why modular**: Easy to add new agents or modify existing ones without touching tasks or crew logic
- **Key functions**:
  - `email_context_analyst()`: Returns configured analyst agent
  - `email_writer()`: Returns configured writer agent

#### **3. `tasks.py` — Task Definitions**
- **Responsibility**: Define what each agent should do, inputs, and expected outputs
- **Why modular**: Task instructions can be updated independently of agent definitions or crew orchestration
- **Key functions**:
  - `analyze_email_task()`: Creates Task 1 (analysis)
  - `write_email_task()`: Creates Task 2 (writing) with context dependency

#### **4. `crew.py` — Workflow Orchestration**
- **Responsibility**: Assemble agents and tasks, configure execution process
- **Why modular**: Changes to workflow order, process type, or memory settings are centralized here
- **Key functions**:
  - `build_email_crew()`: Assembles and returns configured crew

#### **5. `config.py` — Configuration & LLM Setup**
- **Responsibility**: Environment variable loading, LLM initialization, valid options
- **Why modular**: All configuration in one place; easy to switch models, update API keys, or modify valid tones
- **Key functions**:
  - Loads `OPENAI_API_KEY` and `OPENAI_MODEL` from `.env`
  - Initializes `ChatOpenAI` LLM client
  - Maintains `VALID_TONES` list

### Error Handling

The system includes **defensive programming** practices:

```python
# agent.py: Validates API key existence
if not os.getenv("OPENAI_API_KEY"):
    print("OPENAI_API_KEY missing in .env")
    sys.exit(1)
```

```python
# agent.py: Warns about unsupported tones
if values["tone"].lower() not in [t.lower() for t in VALID_TONES]:
    print("Warning: Unknown tone. Continuing...\n")
```

### Scalability Considerations

The modular design supports future expansion:

- **Add new agents**: Define in `agents.py`, create corresponding tasks in `tasks.py`
- **Add preprocessing agents**: Insert new tasks in `crew.py` before writing
- **Add review agent**: Chain another task after writing with output from the writer
- **Tool integration**: CrewAI supports tool binding; can add web search, email sending, etc.
- **Parallel processing**: Switch from `Process.sequential` to `Process.hierarchical` if agents can work independently

### Maintainability

- **Clear naming**: Agent roles, task names, and variable names are self-documenting
- **Minimal dependencies**: Only essential libraries (CrewAI, LangChain, OpenAI)
- **Single responsibility**: Each module handles one concern
- **Configuration centralization**: All settings in `config.py` or `.env`
- **Readable code**: Minimal nesting, clear control flow, docstring-ready structure

---

## 📧 Example Workflow: From Input to Email

### Scenario

User wants to reach out to a potential investor after a coffee chat.

### Command

```bash
python agent.py \
  --context "Met with investor Sarah at startup event; discussed our Series A plans and market opportunity; want to send follow-up" \
  --tone "professional and friendly" \
  --recipient "Sarah (Venture Capitalist)" \
  --sender "Founder"
```

### Step 1: Input Collection
The CLI collects:
- **Context**: "Met with investor Sarah at startup event; discussed Series A plans and market opportunity; want to send follow-up"
- **Tone**: "professional and friendly"
- **Recipient**: "Sarah (Venture Capitalist)"
- **Sender**: "Founder"

### Step 2: Analyst Processing
The Email Context Analyst creates a brief:

```
Purpose: Follow up after initial conversation with investor about Series A fundraising

Key Points:
- Grateful for time and interest shown
- Reiterate market opportunity and growth trajectory
- Express interest in continued conversations
- Propose next steps (call, meeting, materials)

CTA: Schedule a follow-up call or meeting; provide additional information

Subject Suggestion: "Follow-up on Series A Discussion & Market Opportunity"

Writing Style: Professional yet warm; confident but not aggressive; demonstrates competence
```

### Step 3: Writer Processing
The Professional Email Writer transforms the brief into:

```
Subject: Follow-up on Series A Discussion

Dear Sarah,

Thank you so much for taking the time to meet with me at the startup event. I truly appreciated our conversation about our Series A plans and the broader market opportunity in our space.

I'm excited about the potential for collaboration and would love to continue our discussion. Could we schedule a follow-up call next week? I'm happy to share more detailed financial projections or answer any questions you might have.

Looking forward to hearing from you.

Best regards,

Founder
```

### Step 4: Output
The email is displayed to the user, ready to copy into Gmail, Outlook, or any email client.

---

## 📝 Sample Output

Below is a realistic email generated by the system for a professional follow-up scenario:

```
Subject: Follow-up on Marketing Initiative

Dear Ms. Johnson,

Thank you for the valuable insights you shared during our meeting yesterday regarding the new marketing campaign. Your feedback on audience targeting was particularly helpful and has already influenced our strategy adjustments.

I wanted to follow up and confirm our timeline for the next phase of execution. Based on your suggestions, we've refined our approach and believe we can move forward with the revised plan by next Monday.

Please let me know if you have any questions or would like to discuss the revised materials. I'm available for a quick call this week if that would be helpful.

Best regards,

Alex Chen
```

---

## 🚀 Future Improvements

### Implemented Features
- ✅ Multi-agent workflow (analyst + writer)
- ✅ Interactive and non-interactive CLI modes
- ✅ Configurable tone selection
- ✅ Environment-based configuration
- ✅ Crew memory for context passing

### Planned Enhancements

#### Advanced Agents
- **Email Review Agent**: Add a third agent to review emails for tone consistency, grammar, and appropriateness before final output
- **Subject Line Optimizer**: Dedicated agent for A/B testing subject line variations
- **Recipient Context Agent**: Gather information about recipient (role, company) to further personalize tone

#### Content Enhancement
- **HTML Email Generation**: Output HTML-formatted emails for rich text rendering
- **Email Template Library**: Pre-built templates for common scenarios (thank you, apology, negotiation, etc.)
- **Attachment Suggestions**: Recommend documents or files to attach based on email content

#### Integration & Delivery
- **SMTP Integration**: Send emails directly from the CLI
- **Gmail API Integration**: Draft emails directly in Gmail inbox
- **Outlook Integration**: Create draft emails in Outlook
- **Slack Integration**: Trigger email generation from Slack slash commands

#### User Experience
- **Web UI**: Flask/FastAPI web interface for non-technical users
- **Streamlit Dashboard**: Real-time interaction and email preview
- **Batch Processing**: Generate multiple emails from a CSV file
- **Email History**: Store generated emails for retrieval and versioning

#### Developer Experience
- **Structured Logging**: Detailed logs of agent reasoning and decisions
- **Unit Tests**: Test suite for agent outputs and edge cases
- **Docker Support**: Containerized deployment for consistent environments
- **CI/CD Pipeline**: Automated testing and deployment on GitHub Actions
- **API Endpoint**: REST API for programmatic access

#### Quality & Reliability
- **Grammar Checking**: Integrate Grammarly API or open-source grammar tools
- **Tone Detection**: Verify actual output matches requested tone
- **Word Count Enforcement**: Hard limit on email length with optional summarization
- **Feedback Loop**: Allow users to rate generated emails and fine-tune prompts

---

## ⚠️ Limitations

### Current Limitations

1. **No Email Sending**: The system generates emails but doesn't send them. Users must copy-paste into their email client.

2. **Fixed Temperature**: Temperature is set to 0.3 for consistency. For more creative emails, manual code modification is required.

3. **No Persistent Storage**: Generated emails are not stored. Each session starts fresh with no history or retrieval capability.

4. **Single Language**: Designed for English. Multilingual support would require prompt engineering or separate agent configurations.

5. **Limited Context Window**: Uses OpenAI's standard context length limits. Very long email chains or documents may exceed the context window.

6. **No Tool Integration**: Cannot access external tools (web search, file systems, databases) to gather real-time information for personalization.

7. **API Cost**: Each email generation requires two API calls (analyst + writer), incurring cost per execution.

8. **No Authentication**: No user authentication or API key validation beyond existence checking.

9. **Tone Validation**: Unsupported tones produce a warning but don't prevent execution, potentially leading to unexpected outputs.

10. **Model Availability**: Depends on OpenAI API availability and service status.

### Workarounds

- **Email Sending**: Copy output into your email client or pipe output to a custom SMTP script
- **More Creativity**: Modify `temperature` in `config.py` to 0.7 or higher
- **Email History**: Redirect output to a log file: `python agent.py > emails.log`
- **Cost Optimization**: Use `gpt-3.5-turbo` instead of `gpt-4o-mini` for faster, cheaper processing

---

## 🎓 Learning Outcomes

This project demonstrates key software engineering and AI concepts:

### Multi-Agent AI Systems
- How to decompose complex tasks into specialized agents
- Agent orchestration and communication patterns
- Sequential vs. hierarchical execution models
- Task dependencies and context passing

### LLM Orchestration
- Prompt engineering and task specification
- Using LLM APIs responsibly and cost-effectively
- Temperature and model selection for desired output characteristics
- Structured prompts for reproducible outputs

### Architecture & Design
- Separation of concerns (agents, tasks, crew, config)
- Modularity for extensibility and maintainability
- Configuration management (environment variables, defaults)
- Error handling and input validation

### CLI Development
- Argument parsing with argparse
- Interactive user prompts with defaults
- Input validation and user guidance
- Clean output formatting

### Environment & Dependency Management
- Python virtual environments
- pip and requirements.txt for reproducibility
- Environment variable security (.env files)
- Python 3.9+ features and idioms

### API Integration
- OpenAI API usage and best practices
- LangChain abstraction layer benefits
- Async and sequential API calls
- Rate limiting and cost considerations

---

## 🤝 Contributing

We welcome contributions! Whether you're fixing bugs, adding features, or improving documentation, please follow these guidelines:

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally: `git clone https://github.com/YOUR_USERNAME/eAgent.git`
3. **Create a feature branch**: `git checkout -b feature/your-feature-name`
4. **Make your changes** and test thoroughly
5. **Commit with clear messages**: `git commit -m "Add feature: description"`
6. **Push to your fork**: `git push origin feature/your-feature-name`
7. **Open a Pull Request** to the main repository

### Contribution Ideas

- **Bug fixes**: Report or fix issues in agent behavior, CLI handling, or error messages
- **New agents**: Add specialized agents for specific email types (thank you, apology, negotiation, etc.)
- **Output formats**: Add HTML, Markdown, or rich text formatting options
- **Testing**: Write unit tests and integration tests
- **Documentation**: Improve README, add examples, create troubleshooting guides
- **Integrations**: Add Gmail, Slack, or other service integrations
- **Performance**: Optimize prompts for faster execution or lower costs

### Code Standards

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for complex functions
- Keep functions focused and single-purpose
- Test your changes before submitting a PR
- Include example usage in PR descriptions

### Reporting Issues

When reporting bugs or requesting features:
- Provide a clear description of the issue or feature
- Include steps to reproduce (for bugs)
- Attach error messages or logs
- Suggest a solution if you have one

---

## 📄 License

This project is licensed under the **MIT License**, which permits:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

With the requirement that:
- ⚠️ License and copyright notice must be included

See the [LICENSE](LICENSE) file for full terms.

---

## 🙏 Acknowledgements

This project was built using:

- **[CrewAI](https://crewai.com)** — Intelligent agent orchestration framework
- **[OpenAI](https://openai.com)** — GPT-4o-mini language model and API
- **[LangChain](https://langchain.com)** — LLM integration and abstraction layer
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** — Environment variable management

Special thanks to the open-source community for creating and maintaining these foundational tools.

---

## 📞 Support

For questions or issues:
- **GitHub Issues**: Open an issue on [eAgent Issues](https://github.com/19-mohityadav/eAgent/issues)
- **Discussions**: Use [GitHub Discussions](https://github.com/19-mohityadav/eAgent/discussions) for questions

---

**Built with ❤️ by [19-mohityadav](https://github.com/19-mohityadav)**

*Last Updated: 2024*
