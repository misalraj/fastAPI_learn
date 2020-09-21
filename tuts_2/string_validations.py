from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/item/")
async def get_items(item_query: str = Query(..., title="item List", description="list of items",
                                            min_length=2, max_length=10, regex="^item\d{1,6}", deprecated=True,
                                            alias="item-id")):
    return {"item_query": item_query}
