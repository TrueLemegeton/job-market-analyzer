import os

from dotenv import load_dotenv
from openai import OpenAI

from src.config import PROMPT, AI_ROLE


load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.apinex.bond/v1",
)


def get_prompt(system_instructions: str, title: str, description: str, skills: list) -> str:
    prompt = f"""
    Название вакансии: {title}
    Описание вакансии: {description}
    Навыки вакансии: {skills}

    Задание:
    {system_instructions}
    """

    return prompt


def ask_ai(prompt: str, system_prompt: str = AI_ROLE) -> str:
    """Простая обёртка над API."""

    response = client.chat.completions.create(
        model="free/gemini-3.1-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def analyze_vacancy(title: str, description: str, skills: list) -> str:
    """Отправляет вакансию в AI для анализа."""

    prompt = get_prompt(
        system_instructions=PROMPT,
        title=title,
        description=description,
        skills=skills,
    )

    return ask_ai(prompt)