from crewai import Task


def analyze_email_task(agent, context, recipient, tone):

    return Task(
        description=f"""
Analyze the email request.

Context:
{context}

Recipient:
{recipient}

Tone:
{tone}

Provide:

1. Purpose
2. Key Points
3. CTA
4. Subject Suggestion
5. Writing Style
""",
        expected_output="""
A structured brief containing:

- Purpose
- Key Points
- CTA
- Subject
- Writing Style
""",
        agent=agent,
    )


def write_email_task(agent, analysis_task, recipient, tone, sender):

    return Task(
        description=f"""
Write the final email using the analyst's brief.

Requirements:

- Tone: {tone}
- Recipient: {recipient}
- Under 200 words
- Professional formatting

Output Format

Subject: ...

Dear ...

Body

Regards,

{sender}
""",
        expected_output="Complete professional email.",
        context=[analysis_task],
        agent=agent,
    )