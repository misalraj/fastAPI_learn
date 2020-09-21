from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field


class Items(BaseModel):
    name: str = Field(..., title="Name of items", max_length=100)
    price: int
    desc: str = None


app = FastAPI(debug=True)


@app.post("/item/{item_id}")
async def get_item(item: Items = Body(..., embed=True)):
    return {"item": item}
