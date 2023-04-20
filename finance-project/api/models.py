from uuid import UUID
from pydantic import BaseModel, Field


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username, between 6 and 20 chars")
    id: int = Field(description="UUID number")


class UserInfo(OrmModel):
    id: UUID
    username: str
    stocks: list[str]


class AssetAdd(BaseModel):
    ticker: str = Field(description="The ticker symbol for the asset, "
                                    "which is a unique code used to identify it on a stock exchange.")


class AssetInfoBase(OrmModel):
    ticker: str
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
    close_price: float
    fifty_day_price: float
    today_low_price: float
    today_high_price: float
    open_price: float
    evolution: float


class UserInfo(OrmModel):
    id: UUID
    username: str
    stocks: list[AssetInfoBase]

