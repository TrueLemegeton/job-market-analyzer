from src.normalizer.experience import normalize_experience
from src.normalizer.hiring_format import normalize_hiring_format
from src.normalizer.salary import normalize_salary
from src.normalizer.schedule import normalize_schedule
from src.normalizer.work_format import normalize_work_format
from src.normalizer.working_hours import normalize_working_hours


def get_clean_vacancy_data(vacancy: dict) -> dict | None:
    '''Возвращает словарь с чистыми данными.'''
    if vacancy is None:
        return None


    salary = normalize_salary(vacancy['salary'])
    experience = normalize_experience(vacancy['experience'])
    schedule = normalize_schedule(vacancy['schedule'])
    work_format = normalize_work_format(vacancy['work_format'])
    hiring_format = normalize_hiring_format(vacancy['hiring_format'])
    working_hours = normalize_working_hours(vacancy['working_hours'])


    clean_vacancy = {key: value
                    for key, value in vacancy.items()
                    if key not in {
                    'salary',
                    'experience',
                    'schedule',
                    'work_format',
                    'hiring_format',
                    'working_hours',
                    }}



    clean_vacancy.setdefault('salary_from', None)
    clean_vacancy.setdefault('salary_to', None)
    clean_vacancy.setdefault('salary_currency', None)
    clean_vacancy.setdefault('salary_period', None)
    clean_vacancy.setdefault('tax_status', None)
    
    if salary:
        clean_vacancy.update(salary)

    if experience:
        clean_vacancy.update(experience)

    if schedule:
        clean_vacancy.update(schedule)

    if work_format:
        clean_vacancy.update(work_format)

    if working_hours:
        clean_vacancy.update(working_hours)

    if hiring_format:
        clean_vacancy.update(hiring_format)


    return clean_vacancy