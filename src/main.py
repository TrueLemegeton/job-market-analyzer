from playwright.sync_api import sync_playwright

from src.scraper.vacancies import get_vacancies_cards_links
from src.scraper.parser import parse_vacancy
from src.normalizer.salary import normalize_salary


def main():
    with sync_playwright() as playwright:
        for page in range(3):
            links = get_vacancies_cards_links(playwright, page_number=page)

            print(f'Найдено ссылок: {len(links)}')
            print(f'Сраница: {page}')




if __name__ == '__main__':
    main()