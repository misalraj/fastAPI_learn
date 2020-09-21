from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/item/{item_name}")
async def get_item(item_id: str):
    return {"item_id": item_id}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name}


@app.get("/path/{filepath:path}")  # file path in path parameter
async def get_path(filepath: str):
    return {"path": filepath}
