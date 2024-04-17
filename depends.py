from fastapi import Depends, FastAPI
from dependencies import common_parameters
from typing import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons["q"]


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
