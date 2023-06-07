from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

from lf_api.config.database import DbBase


class Client(DbBase):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    addresses = Column(ARRAY(String))
    phone = Column(ARRAY(String))
    emails = Column(ARRAY(String))
    observation = Column(String)
    cpf = Column(String, unique=True)
    cnpj = Column(String, unique=True)
    status_id = Column(Integer, default=1, nullable=False)
