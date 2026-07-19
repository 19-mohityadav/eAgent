from crewai import Crew, Process

from agents import (
    email_context_analyst,
    email_writer,
)

from tasks import (
    analyze_email_task,
    write_email_task,
)


def build_email_crew(context, tone, recipient, sender):

    analyst = email_context_analyst()
    writer = email_writer()

    analyze = analyze_email_task(
        analyst,
        context,
        recipient,
        tone,
    )

    write = write_email_task(
        writer,
        analyze,
        recipient,
        tone,
        sender,
    )

    crew = Crew(
        agents=[
            analyst,
            writer,
        ],
        tasks=[
            analyze,
            write,
        ],
        process=Process.sequential,
        memory=True,
        verbose=False,
    )

    return crew