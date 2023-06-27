from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from client.model import Client, ClientStatus
from config.database import get_db

router = APIRouter()


@router.get('/client')
async def get_client(id=None, db: Session = Depends(get_db)):
    id = 1
    teste = db.query(Client).filter(Client.id == id).first()
    return {'message': 'deu boa'}
