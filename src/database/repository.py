from src.database.models import Vacancy
from sqlalchemy.orm import Session

def save_vacancy(session: Session, vacancy_data: dict) -> None:
    '''Функция для сохранения вакансии в базу данных.'''
    hh_id = vacancy_data.get('hh_id')

    existing_vacancy = session.query(Vacancy).filter_by(hh_id=hh_id).first()

    if existing_vacancy:
        print(f'Вакансия с {hh_id} уже существует в базе данных. Пропуск сохранения.')
        return

    vacancy = Vacancy(
        hh_id=vacancy_data['hh_id'],
        title=vacancy_data['title'],
        company=vacancy_data['company'],
        employment=vacancy_data['employment'],
        link=vacancy_data['link'],
        description=vacancy_data['description'],
        address=vacancy_data['address'],
        payment_frequency=vacancy_data['payment_frequency'],
        collected_at=vacancy_data['collected_at'],
        salary_from=vacancy_data['salary_from'],
        salary_to=vacancy_data['salary_to'],
        salary_currency=vacancy_data['salary_currency'],
        salary_period=vacancy_data['salary_period'],
        tax_status=vacancy_data['tax_status'],
        experience_from=vacancy_data['experience_from'],
        experience_to=vacancy_data['experience_to'],
        is_active=True,
        has_other_options=vacancy_data['has_other_options'],
        by_agreement=vacancy_data['by_agreement'],
        has_night_shifts=vacancy_data['has_night_shifts'],
    )

    session.add(vacancy)
    session.commit()
    print('Вакансия успешно сохранена в базу данных.')