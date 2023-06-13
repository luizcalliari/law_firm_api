from fastapi import FastAPI

from client import crud


app = FastAPI()

app.include_router(crud.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
