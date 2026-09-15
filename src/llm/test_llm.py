from src.llm.service import analyze_vacancy

test_title = "Python Developer"
test_skills = ["Python", "PostgreSQL"]
test_description = """
Ищем Middle Python разработчика. 
Нужен опыт с FastAPI, Docker, Redis и Asyncio. Разговорный английский B1.
"""

print("🚀 Отправляем запрос в нейросеть...\n")

result = analyze_vacancy(
    title=test_title,
    description=test_description,
    skills=test_skills,
)

print("=" * 50)
print("ОТВЕТ НЕЙРОСЕТИ:")
print("=" * 50)
print(result)
print("=" * 50)