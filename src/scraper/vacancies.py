from playwright.sync_api import Playwright

from bs4 import BeautifulSoup

from src.config import URL


def get_vacancies_cards_links(playwright: Playwright, page_number) -> list:
    '''С одной страницы собераются ссылки с каждой карчтоки вакансии.'''
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    page = browser.new_page()
    page.goto(f'{URL}&page={page_number}', wait_until="commit")
    page.wait_for_timeout(10000)

    vacancies = page.locator('article') # [data-qa="vacancy-serp__vacancy"]
    links = []
    print(f'Всего вакансий: {vacancies.count()}')

    for i in range(vacancies.count()):
        vacancy = vacancies.nth(i)

        html = vacancy.evaluate('(element) => element.outerHTML')
        soup = BeautifulSoup(html, 'html.parser')


        link = soup.select_one('[data-qa="serp-item__title"]').get("href")
        links.append(link)

    browser.close()

    return links