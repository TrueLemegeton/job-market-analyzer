import re

def normalize_hiring_format(hiring_format: str | None) -> str | None:
    """Приводит сырой формат оформления к нормализованному виду."""

    if hiring_format is None:
        return None

    hiring_format = hiring_format.lower().strip()
    hiring_format = re.sub(r'\s+', '', hiring_format)

    available_hiring_formats = {
        'трудовойдоговор': 'трудовой договор',
        'ссамозанятым': 'договор гпх с самозанятым',
        'сип': 'договор гпх с ип',
        'сфизлицом': 'договор гпх с физлицом',
    }

    normalized_hiring_format = []

    for key, value in available_hiring_formats.items():
        if key in hiring_format:
            normalized_hiring_format.append(value)

    return {'hiring_format': normalized_hiring_format}



    