import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_TYPE = os.environ.get("DB_TYPE")
DB_LOGIN = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_TABLE = os.environ.get("DB_TABLE")

SQLALCHEMY_DATABASE_URL = f"{DB_TYPE}://{DB_LOGIN}:{DB_PASS}@{DB_HOST}/{DB_TABLE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

