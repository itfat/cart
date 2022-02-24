from typing import List, Optional, Set

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class ItemCreate(ItemBase):
    pass

class OfferBase(BaseModel):
    title: str
    # price: float = Field(..., gt=0, description="The price must be greater than zero")
    item_id: int


class Offer(ItemBase):
    id: int

    class Config:
        orm_mode = True

class OfferCreate(OfferBase):
    pass
    # name: str
    # description: Optional[str] = None
    # price: float
    # items: List[Item]

