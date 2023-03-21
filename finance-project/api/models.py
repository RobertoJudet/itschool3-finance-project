from pydantic import BaseModel, Field


class UserAdd(BaseModel):
    name: str = Field(description="Full name")


class UserInfo(UserAdd):
    stocks: list = Field(description="A list of stocks")
