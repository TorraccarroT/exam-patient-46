from sqlalchemy import String
from sqlalchemy import Column, DateTime, Integer,DATE
from sqlalchemy import  Column, Integer, String
from db import Base

class Patien(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, index=True)
    clinic_name = Column(String(100), index=True)
