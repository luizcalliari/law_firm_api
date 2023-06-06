import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_TYPE = os.environ.get("DB_TYPE")
DB_LOGIN = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_TABLE = os.environ.get("DB_TABLE")

SQLALCHEMY_DATABASE_URL = f"{DB_TYPE}://{DB_LOGIN}:{DB_PASS}@{DB_HOST}/{DB_TABLE}"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DbBase = declarative_base()
