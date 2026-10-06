from fastapi import FastAPI
from schema.patient import Patient
from model import patien as modelp
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db import get_db
app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}