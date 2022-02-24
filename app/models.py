from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Integer, index=True)
    description = Column(String, index=True)

    offer = relationship("Offer", back_populates="items")

class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))   

    items = relationship("Item", back_populates="offer")


