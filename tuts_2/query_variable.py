from fastapi import FastAPI
from pydantic import BaseModel


class Items(BaseModel):
    name: str = "Misal"
    price: int = 100
    desc: str = None


app = FastAPI(debug=True)


@app.post("/item/")
async def get_item(item: Items):
    return item
