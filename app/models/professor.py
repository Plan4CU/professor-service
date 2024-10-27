from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Professor(BaseModel):
    P_UNI: str # required and not nullable,  name of variable: type of variable 
    first_name: str 
    middle_name: Optional[str] = None # you cold have a professor w/o middle name 
    last_name: str
    email: str 

    # how does this work? 
    class Config:
        json_schema_extra = {
            "example": {
                "P_UNI": 12345,
                "first_name": "John",
                "middle_name": "Deez",
                "last_name": "Nutz",
                "email": "123@columbia.edu"
            }
        }
