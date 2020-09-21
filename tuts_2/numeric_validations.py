from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/item/{item}")
async def get_items(item: int = Path(..., title="item List", description="list of items",
                                     gt=1, le=6)):
    return {"item_query": item}
