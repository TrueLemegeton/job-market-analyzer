import re


def normalize_salary(salary: str | None) -> dict:
    '''Из сырого поля с зарплатой вычленяет необходимые поля.'''
    if not salary:
        return None

    salary = salary.lower().strip()

    if not salary:
        return None

    # Поиск цифр
    raw_numbers = re.findall(r'\d+', salary)
    clean_numbers = [int(num) for num in raw_numbers]

    salary_from = None
    salary_to = None
    salary_currency = None
    salary_period = None
    tax_status = None

    # От и до
    if len(clean_numbers) == 2:
        salary_from = clean_numbers[0]
        salary_to = clean_numbers[1]
        type_salary = "Диапазон (от и до)"

    elif len(clean_numbers) == 1:
        if salary.startswith('до'):
            salary_to = clean_numbers[0]
            # type_salary = "Максимальная (до)"

        elif salary.startswith('от'):
            salary_from = clean_numbers[0]
            # type_salary = "Минимальная (от)"

        else:
            salary_from = clean_numbers[0]
            salary_to = clean_numbers[0]
            # type_salary = "Фиксированная"

    # Валюта
    currency_match = re.search(r'₽|\$|so‘m', salary)
    currency = currency_match.group() if currency_match else 'Неизвестно'

    # Период выплат
    period_match = re.search(r'замесяц|зауслугу|зачас|задень', salary)
    if period_match:
        period = period_match.group().replace('за', '')
    else:
        period = 'не указан'

    # на руки или до вычета налогов
    if 'наруки' in salary:
        tax_status = 'На руки'
    elif 'довычетаналогов' in salary:
        tax_status = 'До вычета налогов'
    else:
        tax_status = 'Не указано'

    return {}