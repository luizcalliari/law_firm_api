from pydantic import BaseModel


class ClientStatusBase(BaseModel):
    id: int
    description: str = ""

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    id: int
    name: str
    address: list[str] = []
    phone: list[str] = []
    emails: list[str] = []
    observation: str | None = None
    cpf: str | None = None
    cnpj: str | None = None
    status_id: ClientStatusBase

    class Config:
        orm_mode = True
