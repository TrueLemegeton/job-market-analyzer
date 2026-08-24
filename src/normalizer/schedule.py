import re


def normalize_schedule(schedule: str | None) -> dict | None:
    """Приводит сырой график к нормализованному виду."""

    if schedule is None:
        return None

    normalized_schedule = re.sub(r'\s+', '', schedule.lower().strip())

    available_schedules = {
        '5/2': '5/2',
        '6/1': '6/1',
        '4/4': '4/4',
        '4/3': '4/3',
        '3/3': '3/3',
        'повыходным': 'по выходным',
        'свободный': 'свободный',
    }

    normalized_schedules = []

    for available_schedule in available_schedules:
        if available_schedule in normalized_schedule:
            normalized_schedules.append(available_schedule)

    has_other_options = False

    if re.search(r'и(другиеварианты|ещё\d+)', normalized_schedule):
        has_other_options = True

    return {
        'schedule': normalized_schedules,
        'has_other_options': has_other_options,
    }