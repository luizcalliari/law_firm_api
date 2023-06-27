from fastapi import FastAPI

from client import crud, model
from config.database import engine


app = FastAPI()

app.include_router(crud.router)
model.Base.metadata.create_all(bind=engine)



@app.get("/")
async def root():
    return {"message": "Hello World"}
