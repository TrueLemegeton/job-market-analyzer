from time import sleep
from random import uniform
from playwright.sync_api import sync_playwright

from src.scraper.vacancies import get_vacancies_cards_links, get_vacancy_id
from src.scraper.parser import parse_vacancy
from src.database.database import SessionLocal
from src.database.repository import save_vacancy
from src.normalizer.service import get_clean_vacancy_data


def run_job_scraping_pipeline(page_count: int) -> None:
    '''Запускает пайплайн для сбора вакансий с сайта HeadHunter и сохранения их в базу данных.'''
    session = SessionLocal()
    print('Сессия БД создана.')

    session = SessionLocal()
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
                    print(clean_vacancy['link'])
                    print(clean_vacancy['skills'])
                    save_vacancy(session, clean_vacancy)


                    sleep(uniform(1, 1.5))

    finally:
        session.close()
        print('Сессия закрыта.')