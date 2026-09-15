from src.database.models import HiringFormat, Skill, Vacancy, WorkFormat, Schedule, WorkingHours
from sqlalchemy.orm import Session

def save_vacancy(session: Session, vacancy_data: dict) -> None:
    '''Функция для сохранения вакансии в базу данных.'''
    hh_id = vacancy_data.get('hh_id')
    link = vacancy_data['link']

    if hh_id is not None:
        existing_vacancy = session.query(Vacancy).filter_by(hh_id=hh_id).first()
        if existing_vacancy:
            print(f'Вакансия с таким hh_id: {hh_id} уже существует в базе данных. Пропуск сохранения.')
            return

    else:
        existing_vacancy = session.query(Vacancy).filter_by(link=link).first()
        if existing_vacancy:
            print(f'Вакансия с таким link: {link} уже существует в базе данных. Пропуск сохранения.')
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

    for skill_name in vacancy_data.get('skills', []):
        skill = session.query(Skill).filter_by(name=skill_name).first()

        if skill is None:
            skill = Skill(name=skill_name)
            session.add(skill)
            

        vacancy.skills.append(skill)


    for work_format_name in vacancy_data.get('work_format', []):
        work_format = session.query(WorkFormat).filter_by(name=work_format_name).first()

        if work_format is None:
            
            work_format = WorkFormat(name=work_format_name)
            session.add(work_format)
            

        vacancy.work_formats.append(work_format)


    for schedule_name in vacancy_data.get('schedule', []):
        schedule = session.query(Schedule).filter_by(name=schedule_name).first()

        if schedule is None:
            schedule = Schedule(name=schedule_name)
            session.add(schedule)
            

        vacancy.schedules.append(schedule)


    for hiring_format_name in vacancy_data.get('hiring_format', []):
        hiring_format = session.query(HiringFormat).filter_by(name=hiring_format_name).first()

        if hiring_format is None:
            hiring_format = HiringFormat(name=hiring_format_name)
            session.add(hiring_format)
            

        vacancy.hiring_formats.append(hiring_format)

    for hour in vacancy_data.get('working_hours', []):
        working_hour = session.query(WorkingHours).filter_by(hours=hour).first()
    
        if working_hour is None:
            working_hour = WorkingHours(hours=hour)
            session.add(working_hour)
    
        vacancy.working_hours.append(working_hour)

    session.commit()
    print('Вакансия успешно сохранена в базу данных.')
    print('='*30)