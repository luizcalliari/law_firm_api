from fastapi import APIRouter

from client.model import Client


router = APIRouter()
@router.get('/client')
async def get_client(id=None):
    print('uga uga uga')
    breakpoint()
    return {'message': 'deu boa'}
