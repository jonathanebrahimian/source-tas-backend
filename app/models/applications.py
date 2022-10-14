from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from bson.objectid import ObjectId
from bson import binData
from models.classes import ClassSchema

class Applications(BaseModel):
    email: str = EmailStr
    time: datetime
    resume: binData
    classes: list[ClassSchema]
    

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


class UpdateApplicationsModel(BaseModel):
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
