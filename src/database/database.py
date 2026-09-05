from src.database.models import Base
from src.database.connection import engine
from sqlalchemy.orm import sessionmaker


SessionLocal = sessionmaker(bind=engine)


def create_tables() -> None:
    Base.metadata.create_all(engine)
