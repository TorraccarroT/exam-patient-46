from sqlalchemy import String
from sqlalchemy import Column, DateTime, Integer,DATE
from sqlalchemy import  Column, Integer, String
from db import Base

class Patien(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, index=True)
    hn = Column(String(9), index=True)
    visit_date = Column(DATE)
    symptom = Column(String(255))
    clinic_id = Column(Integer)
