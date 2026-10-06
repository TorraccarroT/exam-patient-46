from fastapi import FastAPI
from schema.patient import Patient
from model import patien as modelp
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db import get_db
app = FastAPI()



@app.get("/users/{user_id}")
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(modelp).where(modelp.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/items/")
async def create_item(item: Patient) -> Patient:
    if len(item.cid) < 13:
        print("ไม่ผ่าน 13")
    return item
@app.get("/")
async def root():
    return {"message": "Hello World"}