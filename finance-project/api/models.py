import uuid

from pydantic import BaseModel, Field


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username, between 6 and 20 chars")
    id: int = Field(description="UUID number")



class UserInfo(BaseModel):
    username: str
    id: int = uuid.uuid4()
    stocks: list[str]

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
