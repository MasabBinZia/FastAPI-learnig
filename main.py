from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greet():
    return "Hello World from FASTAPI ! .... 121"


# path parameters
@app.get("/productItems/{item_id}")
def items(item_id: int):
    return {"id": item_id}


@app.get("/file/file_path:path}")
async def path(file_path: str):
    return {"path": file_path}


@app.get("/{product}/productItems/{item_id}")
def productItems(item_id: int, product: str):
    return {"id": item_id, "productName": product}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item1(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/productItems1/{item_id}")
async def read_item2(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/productItems2/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/productItems3/{item_id}")
async def read_user_item1(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/productItems4/{item_id}")
async def read_user_item2(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
