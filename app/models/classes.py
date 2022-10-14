from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from bson.objectid import ObjectId


class Labs(BaseModel):
    time: datetime
    name: str

class ClassSchema(BaseModel):
    name: str = Field(...)
    active: bool
    labs: Union[list[Labs], None] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "CS 4351",
                "active":True,
                "labs":[{
                    'time':'2032-04-23T10:20:30.400+02:30',
                    'name':'N12'
                },{
                    'time':'2022-04-23T10:20:30.400+02:30',
                    'name':'N13'
                }]
            }
        }


class UpdateClassModel(BaseModel):
    name: Optional[str]
    active: Optional[bool]
    labs: Optional[list[Labs]]

    class Config:
        schema_extra = {
            "example": {
                "name": "CS 4351",
                "active":True,
                "labs":[{
                    'time':'2032-04-23T10:20:30.400+02:30',
                    'name':'N12'
                },{
                    'time':'2022-04-23T10:20:30.400+02:30',
                    'name':'N13'
                }]
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}