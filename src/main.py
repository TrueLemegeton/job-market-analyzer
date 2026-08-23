from playwright.sync_api import sync_playwright, Playwright
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
import random


url = 'https://hh.ru/search/vacancy?text=Python&search_field=name&search_field=company_name&search_field=description&enable_snippets=true&hhtmFrom=main'


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Sec-Ch-Ua': '"Not;A=Brand";v="99", "Chromium";v="128", "Google Chrome";v="128"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"'
}


def get_vacancies_cards_links(playwright: Playwright, page_number) -> list:
    '''С одной страницы собераются ссылки с каждой карчтоки вакансии.'''
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    page = browser.new_page()
    page.goto(f'{url}&page={page_number}', wait_until="commit")
    page.wait_for_timeout(10000)

    vacancies = page.locator('[data-qa="vacancy-serp__vacancy"]')
    links = []
    print(f'Всего вакансий: {vacancies.count()}')

    for i in range(vacancies.count()):
        vacancy = vacancies.nth(i)

        html = vacancy.evaluate('(element) => element.outerHTML')
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.select_one('[data-qa="serp-item__title-text"]')
        link = soup.select_one('[data-qa="serp-item__title"]').get("href")
        links.append(link)

        # print('=' * 50)

        # print(f'{i + 1}. Название: {title.get_text(strip=True)}')
        # print(f'Ссылка: {link}')

    browser.close()

    return links


def get_html(url: str, params=None) -> str | None:
    '''Делает запрос к странице и возвращает HTML.'''
    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=15)

        if response.status_code == 200:
            HTML = response.text
            return HTML
   
        print(f'Ошибка загрузки страницы. Статус: {response.status_code}')


    except requests.RequestException as error:
        print(f'Возникла сетевая ошибка при запросе к {url}: {error}')
        return None


def get_main_information(link: str):
    '''Получает всю необходимую информацию с ссылки одной вакансии.'''
    html = get_html(link)
    soup = BeautifulSoup(html, 'html.parser')




    print('='*50)

    title_element = soup.select_one('[data-qa="vacancy-title"]')

    salary_element_net = soup.select_one('[data-qa="vacancy-salary-compensation-type-net"]')
    salary_element_gross = soup.select_one('[data-qa="vacancy-salary-compensation-type-gross"]')

    company_element = soup.select_one('[data-qa="vacancy-company-name"]')
    work_experience_element = soup.select_one('[data-qa="work-experience-text"]')
    work_schedule_element = soup.select_one('[data-qa="work-schedule-by-days-text"]')
    common_employment_element = soup.select_one('[data-qa="common-employment-text"]')
    work_format_element = soup.select_one('[data-qa="work-formats-text"]')
    vacancy_hiring_format_element = soup.select_one('[data-qa="vacancy-hiring-formats"]')
    key_skills_elements = soup.select('[data-qa="skills-element"]')

    description_element = soup.select_one('[data-qa="vacancy-description"]')
    working_hours_element = soup.select_one('[data-qa="working-hours-text"]')
    compensation_frequency_element = soup.select_one('[data-qa="compensation-frequency-text"]')
    address_element = soup.select_one('[data-qa="vacancy-view-raw-address"]')


    
    title = title_element.get_text(strip=True) if title_element else None

    salary_net = salary_element_net.text if salary_element_net else None
    salary_gross =  salary_element_gross.text if salary_element_gross else None

    company = company_element.text if company_element else None
    work_experience = work_experience_element.text if work_experience_element else None
    work_schedule = work_schedule_element.text if work_schedule_element else None
    common_employment = common_employment_element.text if common_employment_element else None
    work_format = work_format_element.text if work_format_element else None
    vacancy_hiring_format = vacancy_hiring_format_element.text if vacancy_hiring_format_element else None
    key_skills = [skill.get_text(strip=True) for skill in key_skills_elements]
    description = description_element.text if description_element else None
    working_hours = working_hours_element.text if working_hours_element else None
    compensation_frequency = compensation_frequency_element.text if compensation_frequency_element else None
    address = address_element.text if address_element else None
    collected_at = datetime.now()

    
    print(f'Название: {title}')
    print(f'Зарплата: {salary_net if salary_net else salary_gross}')
    print(f'Компания: {company}')
    print(f'{work_experience}')
    print(f'{common_employment}')
    print(f'{work_schedule}')
    print(f'{work_format}')
    print(f'{vacancy_hiring_format}')
    print(f'Ключевые навыки: {key_skills}')
    print(f'Ссылка: {link}')
    print(f'Описание: {description}')
    print(f'Адрес: {address}')
    print(f'Период выплат: {compensation_frequency}')
    print(f'{working_hours}')
    print(f'Дата сбора: {collected_at}')

def main():
    with sync_playwright() as playwright:
        for page in range(3):
            links = get_vacancies_cards_links(playwright, page_number=page)

            print(f'Найдено ссылок: {len(links)}')
            print(f'СТРАНИЦА: {page}')
            print(f'СТРАНИЦА: {page}')
            print(f'СТРАНИЦА: {page}')
            print(f'СТРАНИЦА: {page}')

            for link in links:
                print('='*50)

                get_main_information(link)

                delay = random.uniform(2, 2.5)
                time.sleep(delay)
    

if __name__ == '__main__':
    main()