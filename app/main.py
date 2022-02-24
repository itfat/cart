from typing import List
from urllib import response

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post("/items/add/", response_model=schemas.Item)
def add_items(
    item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.add_item(db=db, item=item)

@app.post("/offers/create")
async def create_offer(offer: schemas.OfferCreate):
    return offer

@app.get("/offers/", response_model=List[schemas.Item])
def get_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = crud.get_offers(db, skip=skip, limit=limit)
    return offers