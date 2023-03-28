from uuid import UUID

from pydantic import BaseModel, Field


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username, between 6 and 20 chars")
    id: int = Field(description="UUID number")


class UserInfo(BaseModel):
    id: UUID
    username: str
    stocks: list[str]

    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class AssetInfo(BaseModel):
    ticker: str
    units: float
    name: str
    country: str
