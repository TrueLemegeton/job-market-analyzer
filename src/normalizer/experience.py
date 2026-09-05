import re


def normalize_experience(experience) -> dict | None:
    """Приводит сырой формат опыта к нормализованному виду."""

    default_result = {
        'experience_from': None,
        'experience_to': None
    }

    if not experience:
        return default_result


    experience = experience.lower().strip()
    experience = re.sub(r'\s+', '', experience)

    raw_numbers = re.findall(r'\d+', experience)
    clean_numbers = [int(num) for num in raw_numbers]

    experience_from = None
    experience_to = None


    if len(clean_numbers) == 2:
        experience_from = clean_numbers[0]
        experience_to = clean_numbers[1]
    elif 'нетребуется' in experience:
        experience_from = 0
        experience_to = 0   
    elif len(clean_numbers) == 1:
        experience_from = clean_numbers[0]

    return {
        'experience_from': experience_from,
        'experience_to': experience_to
    }

    