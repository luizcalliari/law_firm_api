from sqlalchemy import Column, DefaultClause, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from config.database import DbBase


class Client(DbBase):
    __tablename__ = "client"

    id = Column(Integer, server_default=DefaultClause("nextval('client_id_seq'::regclass)"), primary_key=True, index=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    addresses = Column(ARRAY(String))
    phone = Column(ARRAY(String))
    emails = Column(ARRAY(String))
    observation = Column(String)
    cpf = Column(String, unique=True)
    cnpj = Column(String, unique=True)
    status_id = Column(Integer, ForeignKey('client_status.id'), default=1, nullable=False)


class ClientStatus(DbBase):
    __tablename__ = "client_status"

    id = Column(Integer, server_default=DefaultClause("nextval('client_status_id_seq'::regclass)"), primary_key=True, index=True, nullable=False)
    description = Column(String, unique=True, nullable=False)
    clients = relationship('Client', back_populates='client_status')
