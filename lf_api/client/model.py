from config.database import Base
from pydantic import BaseModel
from sqlalchemy import Column, DefaultClause, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship


class Client(Base):
    __tablename__ = "client"

    id = Column(
        Integer,
        server_default=DefaultClause("nextval('client_id_seq'::regclass)"),
        primary_key=True,
        index=True,
        nullable=False,
    )
    name = Column(String, unique=True, nullable=False)
    addresses = Column(ARRAY(String))
    phones = Column(ARRAY(String))
    emails = Column(ARRAY(String))
    observation = Column(String)
    cpf = Column(String, unique=True)
    cnpj = Column(String, unique=True)
    status_id = Column(
        Integer, ForeignKey("client_status.id"), default=1, nullable=False
    )
    status = relationship("ClientStatus")

    def __init__(
        self,
        name,
        addresses,
        phones,
        emails,
        observation,
        cpf,
        cnpj,
        status_id,
    ):
        self.name = name
        self.addresses = addresses
        self.phones = phones
        self.emails = emails
        self.observation = observation
        self.cpf = cpf
        self.cnpj = cnpj
        self.status_id = status_id


class ClientStatus(Base):
    __tablename__ = "client_status"

    id = Column(
        Integer,
        server_default=DefaultClause(
            "nextval('client_status_id_seq'::regclass)"
        ),
        primary_key=True,
        index=True,
        nullable=False,
    )
    description = Column(String, unique=True, nullable=False)


class ClientResponse(BaseModel):
    name: str
    addresses: list | None
    emails: list | None
    observation: str | None
    cpf: str | None
    cnpj: str | None
    status: str

    class Config:
        orm_mode = True


class ClientUpdate(BaseModel):
    name: str
    addresses: list | None
    emails: list | None
    phones: list | None
    observation: str | None
    cpf: str | None
    cnpj: str | None
    status: str
