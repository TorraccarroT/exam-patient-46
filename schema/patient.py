from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator,ValidationError
from typing import Optional
from datetime import date
from enum import Enum, IntEnum


class GenderEnum(IntEnum):
    Male = 1
    Female =2


class Patient(BaseModel):
    hn : str
    cid : str
    prefix: str
    first_name: str
    last_name: str
    gender: GenderEnum
    birth_date:date
    phone: Optional[int] 
    address :Optional[str] 

    