from crewai import Agent
from config import llm


def email_context_analyst():
    return Agent(
        role="Email Context Analyst",
        goal="Understand the email request and create a structured brief.",
        backstory=(
            "You analyze email requests, identify objectives, "
            "extract important information, and prepare instructions "
            "for the email writer."
        ),
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )


def email_writer():
    return Agent(
        role="Professional Email Writer",
        goal="Write concise and professional emails.",
        backstory=(
            "You are an experienced business copywriter capable of "
            "writing polished emails that achieve their intended goal."
        ),
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )