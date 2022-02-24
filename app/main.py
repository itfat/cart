from typing import List
from urllib import response

from django import db

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

@app.post("/offers/create", response_model=schemas.Offer)
def create_offer(offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    return crud.create_offer(db=db, offer=offer)

@app.get("/offers/", response_model=List[schemas.Offer])
def get_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = crud.get_offers(db, skip=skip, limit=limit)
    return offers

# @app.post("/offers/{offer_name}")
# async def get_offer(offer_name: schemas.Offeroffer):
#     if offer_name == schemas.Offeroffer.buy_one:
#         return {"offer_name": offer_name, "message": "buy one get one offer!"}

#     if offer_name == schemas.Offeroffer.discount_ten:
#         return {"offer_name": offer_name, "message": "ten percent discount on item"}
#     if offer_name == schemas.Offeroffer.discount_fifty:
#         return {"offer_name": offer_name, "message": "fifty percent discount on item"}

@app.post("/cart/add/{item_id}", dependencies=[Depends(get_db)])
def add_to_cart(item_id:int, add: schemas.AddToCart, db: Session = Depends(get_db)):
    item = crud.get_item_by_id(db=db, item_id=item_id)
    return crud.add_item_to_cart(db=db,item=item)

    content = {'message': 'Add to cart.'}
    return cart
    # return HTTPException(status_code=response, content=content)


# @app.get('/cart/', response_model=schemas.Carts)
# async def carts():
#     total_price = 0
#     for item in items:
#         total_price += float(item['item_price'])

#     return {'total_price': total_price, 'items': items}


# @app.delete('/clear')
# async def clear_cart(user: User = Depends(get_current_user)):
#     Cart.delete_all_carts(user.id)
#     content = {'message': 'Clear carts.'}
#     return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=content)


# @app.delete('/delete-item-cart/{row_id}')
# async def delete_item_cart(row_id: str, user: User = Depends(get_current_user)):
#     Cart.delete_cart(user.id, row_id)
#     content = {'message': 'Delete item cart.'}
#     return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=content)