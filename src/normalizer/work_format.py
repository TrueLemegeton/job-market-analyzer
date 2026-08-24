def normalize_work_format(work_format: str) -> dict | None:
    """Приводит сырой формат работы к нормализованному виду."""

    if work_format is None:
        return None

    available_formats = [
        'на месте работодателя',
        'удалённо',
        'гибрид',
        'разъездной',
    ]

    normalized_formats = []

    for work_format_name in available_formats:
        if work_format_name in work_format:
            normalized_formats.append(work_format_name)

    return {
        'work_format': normalized_formats
    }