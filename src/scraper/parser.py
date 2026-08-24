from datetime import datetime

import requests
from bs4 import BeautifulSoup

from src.config import HEADERS


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


def parse_vacancy(link: str):
    '''Получает всю необходимую информацию с ссылки одной вакансии.'''
    html = get_html(link)
    soup = BeautifulSoup(html, 'html.parser')

    key_skills_elements = soup.select('[data-qa="skills-element"]')
    key_skills = [skill.get_text(strip=True) for skill in key_skills_elements]

    title = get_text(soup, '[data-qa="vacancy-title"]')

    salary_net = get_text(soup, '[data-qa="vacancy-salary-compensation-type-net"]')
    salary_gross = get_text(soup, '[data-qa="vacancy-salary-compensation-type-gross"]')

    company = get_text(soup, '[data-qa="vacancy-company-name"]')
    work_experience = get_text(soup, '[data-qa="work-experience-text"]')
    work_schedule = get_text(soup, '[data-qa="work-schedule-by-days-text"]')
    common_employment = get_text(soup, '[data-qa="common-employment-text"]')
    work_format = get_text(soup, '[data-qa="work-formats-text"]')
    vacancy_hiring_format = get_text(soup, '[data-qa="vacancy-hiring-formats"]')
    description = get_text(soup, '[data-qa="vacancy-description"]')
    working_hours = get_text(soup, '[data-qa="working-hours-text"]')
    compensation_frequency = get_text(soup, '[data-qa="compensation-frequency-text"]')
    address = get_text(soup, '[data-qa="vacancy-view-raw-address"]')
    collected_at = datetime.now()

    return {
        'title': title,
        'salary': salary_net if salary_net else salary_gross,
        'company': company,
        'experience': work_experience,
        'employment': common_employment,
        'schedule': work_schedule,
        'work_format': work_format,
        'hiring_format': vacancy_hiring_format,
        'skills': key_skills,
        'link': link,
        'description': description,
        'address': address,
        'payment_frequency': compensation_frequency,
        'working_hours': working_hours,
        'collected_at': collected_at,
    }


def get_text(soup: BeautifulSoup, selector: str) -> str | None:
    '''Находит элемент по CSS-селектору и возвращает его текст.'''
    element = soup.select_one(selector)

    if element:
        return element.get_text(strip=True)

    return None