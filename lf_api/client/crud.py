from http import HTTPStatus

from client.model import Client, ClientResponse, ClientStatus, ClientUpdate
from config.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/client/{client_id}", response_model=list[ClientResponse])
@router.get("/client", response_model=list[ClientResponse])
async def get_client(
    client_id: int | None = None, db: Session = Depends(get_db)
) -> list:
    """Return the list with the clients data.

    Args:
        client_id (Optional[int]): id of the client.

    Returns:
         Name, addresses, emails, observation and cpf, cnpj and status from the
         client.
    """
    clients = (
        db.query(Client)
        .with_entities(
            Client.name,
            Client.addresses,
            Client.emails,
            Client.observation,
            Client.cpf,
            Client.cnpj,
            ClientStatus.description.label("status"),
        )
        .join(ClientStatus, Client.status_id == ClientStatus.id)
    )

    if client_id:
        clients = clients.filter(Client.id == client_id)

    return clients.all()


@router.put("/client/{client_id}", response_model=ClientResponse)
async def put_client(
    client_id: int, client_data: ClientUpdate, db: Session = Depends(get_db)
) -> list:
    """Update clients data.

    Args:
        client_id (int): id of the client.

    Returns:
         Name, addresses, emails, observation and cpf, cnpj and status from the
         client.
    """
    try:
        client_data = client_data.dict()

        client_status_description = client_data["status"]
        del client_data["status"]

        client_data["status_id"] = (
            db.query(ClientStatus)
            .filter(ClientStatus.description == client_status_description)
            .with_entities(ClientStatus.id)
            .as_scalar()
        )

        client = (
            db.query(Client).filter(Client.id == client_id).update(client_data)
        )
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Invalid input data.",
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=HTTPStatus.INTERNAL_SERVER_ERROR.description,
        )

    client = (
        db.query(Client)
        .with_entities(
            Client.name,
            Client.addresses,
            Client.emails,
            Client.observation,
            Client.cpf,
            Client.cnpj,
            ClientStatus.description.label("status"),
        )
        .join(ClientStatus, Client.status_id == ClientStatus.id)
        .filter(Client.id == client_id)
        .first()
    )

    return client


@router.post("/client", response_model=ClientResponse)
async def post_client(
    client_data: ClientUpdate, db: Session = Depends(get_db)
) -> list:
    """Add new client.

    Returns:
         Name, addresses, emails, observation and cpf, cnpj and status from the
         client.
    """
    try:
        client_data = client_data.dict()

        client_status_description = client_data["status"]
        del client_data["status"]

        client_data["status_id"] = (
            db.query(ClientStatus)
            .filter(ClientStatus.description == client_status_description)
            .with_entities(ClientStatus.id)
            .one()
            .id
        )

        client = Client(**client_data)
        db.add(client)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail="Invalid input data.",
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=HTTPStatus.INTERNAL_SERVER_ERROR.description,
        )

    client = (
        db.query(Client)
        .with_entities(
            Client.name,
            Client.addresses,
            Client.emails,
            Client.observation,
            Client.cpf,
            Client.cnpj,
            ClientStatus.description.label("status"),
        )
        .join(ClientStatus, Client.status_id == ClientStatus.id)
        .filter(Client.id == client.id)
        .first()
    )

    return client
