from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalachemy.orm import relationship

from lf_api.config.database import DbBase


class Client(DbBase):
    __tablename__ = "client"

    seq = DbBase.Sequence('client_id_seq')
    id = Column(Integer, seq, server_default=seq.next_value(), primary_key=True, index=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    addresses = Column(ARRAY(String))
    phone = Column(ARRAY(String))
    emails = Column(ARRAY(String))
    observation = Column(String)
    cpf = Column(String, unique=True)
    cnpj = Column(String, unique=True)
    status_id = Column(Integer, default=1, nullable=False, ForeignKey='client_status.id')


class ClientStatus(DbBase):
    __tablename__ = "client_status"

    seq = DbBase.Sequence('client_id_seq')
    id = Column(Integer, seq, server_default=seq.next_value(), primary_key=True, index=True, nullable=False)
    description = Column(String, unique=True, nullable=False)
    clients = relationship('Client', back_populates = 'client_status')
