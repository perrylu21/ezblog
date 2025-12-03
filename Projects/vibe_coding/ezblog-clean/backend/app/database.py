import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()

# Example: postgresql+psycopg2://user:password@localhost:5432/dbname
# Default uses role 'chao-peilu' and database 'chao-peilu' on localhost.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://chao-peilu:@localhost:5431/chao-peilu",
)

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


