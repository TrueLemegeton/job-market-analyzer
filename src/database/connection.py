import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine


load_dotenv()


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)

engine = create_engine(DATABASE_URL)


with engine.connect() as connection:
    print("Подключение успешно!")