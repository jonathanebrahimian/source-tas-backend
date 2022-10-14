from fastapi import FastAPI, Depends

from app.routes.classes import router as ClassRouter
from fastapi.security import OAuth2PasswordBearer

from logzero import logger

app = FastAPI()

app.include_router(ClassRouter, tags=["Class"], prefix="/class")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
