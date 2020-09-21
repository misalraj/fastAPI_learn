from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PackageIn(BaseModel):
    secret_id: int
    name: str
    item: int
    desc: Optional[str] = None


class Package(BaseModel):
    name: str
    item: int
    desc: Optional[str]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_items(item_id: int):
    return {"item_id": item_id}


@app.get("/items")
async def query_items(item_id: int, item_query: Optional[str]):
    return {"item_id": item_id, "item_query": item_query}


@app.post("/package/{package_id}")
async def create_package(package_id: int, package: Package, text: str):
    return {"package_id": package_id, "package": package, "Text": text}


@app.post("/response_package", response_model=Package, response_model_exclude_unset=True,
          response_model_exclude={"name"})
async def response_package(package: PackageIn):
    return package
