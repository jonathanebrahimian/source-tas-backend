from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from bson.objectid import ObjectId
from app.models.classes import ClassSchema

class ApplicationSchema(BaseModel):
    email: str = EmailStr
    name: str
    time: datetime
    resume: str
    classes: list[ClassSchema]
    

    class Config:
        schema_extra = {
            "example": {
                "email": "jdoe@mail.com",
                "name": "John Doe",
                "time": "2021-09-01T00:00:00",
                "resume": "resume.pdf",
                "classes":[{
                    'time':'2032-04-23T10:20:30.400+02:30',
                    'name':'N12'
                },{
                    'time':'2022-04-23T10:20:30.400+02:30',
                    'name':'N13'
                }]
            }
        }


class UpdateApplicationModel(BaseModel):
    email: Optional[str] = EmailStr
    name: Optional[str]
    time: Optional[datetime]
    resume: Optional[str]
    classes: Optional[list[ClassSchema]]

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
