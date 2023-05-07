from pydantic import BaseModel, Field
from uuid import UUID


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars")

class BaseInfo(BaseModel):
    class Config:
        orm_mode = True

class UserInfo(BaseInfo):
    id: UUID
    username: str
    stocks: list[str]

class AssetInfoBase(BaseInfo):
    ticker: str
    units: float
    name: str
    country: str

class AssetInfoUser(AssetInfoBase):
    units: float

class AssetInfoPrice(AssetInfoBase):
    current_price: float
    currency: str
    today_low_price: float
    today_high_price: float
    open_price: float
    closed_price: float
    fifty_day_price: float
    price_change_percent: str



