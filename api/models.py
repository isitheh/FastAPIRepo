#Perform import

import uuid
from pydantic import BaseModel, Field

#Define Task Model
#This model is used to create anew task - A new task needs an ID.
class TaskModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4(), alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    is_finished: bool = Field(...)

    #The config class allows us to document our models schema
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "My task name",
                "description": "My description",
                "is_finished": False
            }
        }

#Define Task Update Model
#This model is used to update a selected task. ID is never to be updated.
class TaskUpdateModel(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    is_finished: bool = Field(...)

    # The config class allows us to document our models schema
    class Config:
        schema_extra = {
            "example": {
                "name": "My task name",
                "description": "My description",
                "is_finished": False
            }
        }