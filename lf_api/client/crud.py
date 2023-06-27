from client.model import Client, ClientStatus
from config.database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/client")
async def get_client(id=None, db: Session = Depends(get_db)):
    id = 1
    teste = db.query(Client).filter(Client.id == id).first()
    return {"message": "deu boa"}
