from __future__ import annotations

from pydantic import BaseModel


# data model
# middle_name: Optional[str] = None # you cold have a professor w/o middle name 
# required and not nullable,  name of variable: type of variable 
class Professor(BaseModel):
    p_uni: str
    first_name: str
    last_name: str

    # how does this work? 
    class Config:
        json_schema_extra = {
            "example": {
                "p_uni": "Cheese123",
                "first_name": "John",
                "last_name": "Nutz",
            }
        }
