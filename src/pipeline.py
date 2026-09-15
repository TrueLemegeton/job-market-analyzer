from time import sleep
from random import uniform
from playwright.sync_api import sync_playwright

from src.scraper.vacancies import get_vacancies_cards_links, get_vacancy_id
from src.scraper.parser import parse_vacancy
from src.database.database import SessionLocal, clear_tables
from src.database.repository import save_vacancy
from src.normalizer.service import get_clean_vacancy_data
from src.llm.service import analyze_vacancy

def run_job_scraping_pipeline(page_count: int) -> None:
    '''Запускает пайплайн для сбора вакансий с сайта HeadHunter и сохранения их в базу данных.'''
    session = SessionLocal()
    print('Сессия БД создана.')
    
    # clear_tables()
    print('Сессия создана.')

    try:
        with sync_playwright() as playwright:
            for page in range(page_count):
                links = get_vacancies_cards_links(playwright, page_number=page)

                for link in links:
                    vacancy = parse_vacancy(link)

                    if vacancy is None:
                        continue

                    vacancy['hh_id'] = get_vacancy_id(link)

                    clean_vacancy = get_clean_vacancy_data(vacancy)

                    if clean_vacancy['title'] is None:
                        print('Вакансия пропущена. Причина неизвестна.')
                        continue

                    # --- ЭТАП LLM АНАЛИЗА ---
                    try:
                        print(f"\n🔍 Анализируем через AI: {clean_vacancy['title']}")
                        print(f'Ссылка: {clean_vacancy['link']}')
                        print(f'Описание: {clean_vacancy['description']}')
                        ai_analysis = analyze_vacancy(
                            title=clean_vacancy['title'],
                            description=clean_vacancy.get('description', ''),
                            skills=clean_vacancy.get('skills', [])
                        )

                        print("🤖 [LLM Output]:")
                        print(ai_analysis)
                        print("-" * 40)
                        


                        # Добавляем результат анализа в словарь перед сохранением
                        clean_vacancy['ai_analysis'] = ai_analysis
                    except Exception as e:
                        print(f"Ошибка при вызове LLM для {link}: {e}")
                        clean_vacancy['ai_analysis'] = None


                    
                    # save_vacancy(session, clean_vacancy)


                    sleep(uniform(1.5, 2.0))
            

    finally:
        session.close()
        print('Сессия закрыта.')