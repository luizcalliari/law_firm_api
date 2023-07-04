from client.model import Client, ClientResponse, ClientStatus
from config.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/client/{client_id}", response_model=list[ClientResponse])
@router.get("/client", response_model=list[ClientResponse])
async def get_client(
    client_id: int | None = None, db: Session = Depends(get_db)
) -> list:
    clients = db.query(Client).with_entities(
        Client.name, Client.addresses, Client.emails, Client.observation, Client.cpf
    )

    if client_id:
        clients = clients.filter(Client.id == client_id)

    return clients.all()
