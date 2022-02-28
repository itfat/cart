from enum import Enum
from tkinter.tix import Form
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

# class OfferList(str, Enum):

#     buy_one = "buy one get one"
#     discount_ten = "10 percent discount"
#     discount_fifty = "50 percent discount"

class OfferBase(BaseModel):
    item_id: int
    # offer: OfferList = Field(title="Offer")
    title: str


class Offer(OfferBase):
    id: int

    class Config:
        orm_mode = True

class OfferCreate(OfferBase):
    pass
   
    

class AddToCart(BaseModel):
    item_id: int
    quantity: int


class CartItems(BaseModel):
    item_id: str
    item_price: str
    item_quantity: str
    row_id: str


class Carts(BaseModel):
    total_price: float
    items: List[CartItems] = []

    class Config:
        orm_mode = True


