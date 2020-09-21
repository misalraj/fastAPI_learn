from fastapi import FastAPI
from pydantic import BaseModel


class Items(BaseModel):
    name: str
    price: int
    desc: str = None


class User(BaseModel):
    username: str
    full_name: str


app = FastAPI(debug=True)


@app.post("/item/{item_id}")
async def get_item(item_id: int, item: Items, user: User):
    return {"item": item, "user": user}
