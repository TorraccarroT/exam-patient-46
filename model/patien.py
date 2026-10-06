from sqlalchemy import String
from sqlalchemy import Column, DateTime, Integer,DATE
from sqlalchemy import  Column, Integer, String
from db import Base

class Patien(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, index=True)
    hn = Column(String(9), index=True,nullable=False)
    cid = Column(String(13), index=True)
    prefix = Column(String(20), index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    gender = Column(String(2))
    birth_date = Column(DATE)
    phone = Column(String(10),nullable=True)
    address = Column(String(255),nullable=True)
    created_at= Column(DateTime)
    updateed_at= Column(DateTime)
