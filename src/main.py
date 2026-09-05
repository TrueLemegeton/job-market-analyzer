from src.pipeline import run_job_scraping_pipeline


def main() -> None:
    '''Главная функция для запуска анализа вакансий.'''
    print("Запуск сбора вакансий...")
    run_job_scraping_pipeline(page_count=1)
    print("Процесс успешно завершен.")


if __name__ == '__main__':
    main()


