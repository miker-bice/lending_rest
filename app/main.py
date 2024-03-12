from fastapi import FastAPI
from .routers import loans, users
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(loans.router)
# app.include_router(users.router)

@app.get("/")
async def root():
    return {'message': 'hello new world!'}
