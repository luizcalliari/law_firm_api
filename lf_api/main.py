from client import crud, model
from config.database import engine
from fastapi import FastAPI

app = FastAPI()

app.include_router(crud.router)
model.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
