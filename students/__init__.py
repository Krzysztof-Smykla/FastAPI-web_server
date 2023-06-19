# __init__.py
from fastapi import FastAPI
from .router import router

app = FastAPI()

app.include_router(router, prefix="/students")
