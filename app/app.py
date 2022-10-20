from fastapi import FastAPI, Depends

from app.routes.classes import router as ClassRouter
from app.routes.auth import router as AuthRouter


from app.routes import auth
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from logzero import logger

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(user.router, tags=['Users'], prefix='/api/users')
app.include_router(ClassRouter, tags=["Class"], prefix="/class")
app.include_router(AuthRouter, tags=['Auth'], prefix='/api/auth')

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
