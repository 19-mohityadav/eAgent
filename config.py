import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

VALID_TONES = [
    "professional",
    "professional and friendly",
    "friendly",
    "formal",
    "casual",
    "persuasive",
]

llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0.3,
)