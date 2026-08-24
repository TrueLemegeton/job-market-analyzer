from playwright.sync_api import sync_playwright

from src.scraper.vacancies import get_vacancies_cards_links
from src.scraper.parser import parse_vacancy
from src.normalizer.salary import normalize_salary


def print_vacancy(vacancy: dict) -> None:
    '''Печатает всю доступную информацию о вакансии кроме описания.'''
    print('=' * 60)
    print(f"Название: {vacancy['title']}")
    print(f"Компания: {vacancy['company']}")
    print(f"Зарплата: {vacancy['salary']}")
    print(f"Опыт: {vacancy['experience']}")
    print(f"Занятость: {vacancy['employment']}")
    print(f"График: {vacancy['schedule']}")
    print(f"Формат работы: {vacancy['work_format']}")
    print(f"Формат найма: {vacancy['hiring_format']}")
    print(f"Ключевые навыки: {vacancy['skills']}")
    print(f"Адрес: {vacancy['address']}")
    print(f"Период выплат: {vacancy['payment_frequency']}")
    print(f"Рабочие часы: {vacancy['working_hours']}")
    print(f"Ссылка: {vacancy['link']}")
    print(f"Дата сбора: {vacancy['collected_at']}")
    print(f"Описание: {vacancy['description']}")
    print('=' * 60)


def main():
    with sync_playwright() as playwright:

        for page in range(3):
            links = get_vacancies_cards_links(playwright, page_number=page)

            print(f'Страница: {page}')
            print(f'Найдено вакансий: {len(links)}')

            for link in links:
                vacancy = parse_vacancy(link)

                normalized_salary = normalize_salary(vacancy['salary'])

                # print_vacancy(vacancy)

                print('Нормализированная зарплата: ')
                print(normalized_salary)



if __name__ == '__main__':
    main()