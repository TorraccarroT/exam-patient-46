from fastapi import FastAPI
from pydantic import BaseModel,Field,field_validator,ValidationError
from typing import Optional
from datetime import date
from enum import Enum, IntEnum


class lib_clinic(BaseModel):
    clinic_name : str
    