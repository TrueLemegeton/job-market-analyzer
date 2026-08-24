from playwright.sync_api import sync_playwright

from src.scraper.vacancies import get_vacancies_cards_links
from src.scraper.parser import parse_vacancy
from src.normalizer.salary import normalize_salary
from src.normalizer.experience import normalize_experience
from src.normalizer.schedule import normalize_schedule
from src.normalizer.working_hours import normalize_working_hours

from time import sleep
from random import uniform


def print_vacancy(vacancy: dict) -> None:
    '''Печатает всю доступную информацию о вакансии кроме описания.'''
    print('=' * 60)
    print(f"Название: {vacancy['title']}")
    print(f"Компания: {vacancy['company']}")
    print(f"Зарплата: {vacancy['salary']}")
    print(f"{vacancy['experience']}") # опыт работы
    print(f"Занятость: {vacancy['employment']}")
    print(f"{vacancy['schedule']}") # график
    print(f"{vacancy['work_format']}") # формат работы
    print(f"{vacancy['hiring_format']}") # формат найма
    print(f"Ключевые навыки: {vacancy['skills']}")
    print(f"Адрес: {vacancy['address']}")
    print(f"{vacancy['payment_frequency']}") # период выплат
    print(f"{vacancy['working_hours']}") # рабочие часы
    print(f"Ссылка: {vacancy['link']}")
    print(f"Дата сбора: {vacancy['collected_at']}")
    # print(f"Описание: {vacancy['description']}")
    print('=' * 60)


def main():
    with sync_playwright() as playwright:

        for page in range(1):
            links = get_vacancies_cards_links(playwright, page_number=page)

            print(f'Страница: {page}')
            print(f'Найдено вакансий: {len(links)}')

            for link in links:
                vacancy = parse_vacancy(link)

                if vacancy is None:
                    continue


                print(f"Сырой час: {vacancy['hiring_format']}")
                # print(f'Нормализированный час: {normalize_working_hours(vacancy['working_hours'])}')
                
                
                


            sleep(uniform(2, 2.5))


if __name__ == '__main__':
    main()