from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greet():
    return "Hello World from FASTAPI ! .... 121"


# path parameters
@app.get("/items/{item_id}")
def items(item_id: int):
    return {"id": item_id}


@app.get("/file/file_path:path}")
async def path(file_path: str):
    return {"path": file_path}


@app.get("/{product}/items/{item_id}")
def productItems(item_id: int, product: str):
    return {"id": item_id, "productName": product}
