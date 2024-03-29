from fastapi import FastAPI, Body
from models import Item


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    # stor data in DB
    return item.name


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.post("/productitems/")
async def read_item(item: str = Body(embed=True)):
    return item
