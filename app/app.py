from fastapi import FastAPI, Depends

from app.routes.classes import router as ClassRouter
from app.routes.applications import router as ApplicationRouter
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from logzero import logger

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*']
)
app.include_router(ClassRouter, tags=["Class"], prefix="/class")
app.include_router(ApplicationRouter, tags=["Application"], prefix="/application")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
