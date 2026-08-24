import re

def normalize_working_hours(working_hours: str | None) -> dict | None:
    """Приводит сырые рабочие часы работы к нормализованному виду."""
    if working_hours is None:
        return None

    working_hours = re.sub(r'\s+', '', working_hours.lower().strip())
    hours = re.findall(r'\d+', working_hours)
    clean_hours = [int(hour) for hour in hours]

    by_agreement = False
    has_other_options = False
    has_night_shifts = False

    if 'иещё' in working_hours:
        has_other_options = True
        clean_hours.pop()
    if 'подоговорённости' in working_hours:
        by_agreement = True
    if 'вечерниеилиночныесмены' in working_hours:
        has_night_shifts = True

    return {'working_hours': clean_hours,
            'has_other_options': has_other_options,
            'by_agreement': by_agreement,
            'has_night_shifts': has_night_shifts}
