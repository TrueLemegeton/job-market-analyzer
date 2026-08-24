def normalize_hiring_format(hiring_format:str | None) -> str | None:
    """Приводит сырой формат оформления к нормализованному виду."""

    if hiring_format is None:
        return None

    available_hiring_formats = [
    'трудовой договор',
    'договор гпх с самозанятым',
    'договор гпх с ип',
    'договор гпх с физлицом',
    ]

    