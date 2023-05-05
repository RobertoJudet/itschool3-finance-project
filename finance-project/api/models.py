from pydantic import BaseModel, Field


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username, between 6 and 20 chars")


class UserInfo(BaseModel):
    username: str
    stocks: list[str]

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
