from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_TYPE = "postgresql"
DB_LOGIN = "postgres"
DB_PASS = "postgres"
DB_HOST = "lf_psql"
DB_NAME = "lf000"

SQLALCHEMY_DATABASE_URL = f"{DB_TYPE}://{DB_LOGIN}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DbBase = declarative_base()
