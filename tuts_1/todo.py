from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    id: int
    desc: Optional[str]


app = FastAPI(title="Todo App", version="v1", debug=True)

store_todo = []


@app.get("/")
async def get_root():
    return {"list_length": len(store_todo), "list": store_todo}


@app.post("/todo")
async def add_todo(todo: Todo):
    store_todo.append(todo)
    return "todo added"


@app.put("/todo/{ids}")
async def update_todo(ids: int, todo: Todo):
    try:
        store_todo[ids] = todo
        return store_todo
    except:
        raise HTTPException(status_code=400, detail="Todo not found")


@app.delete("/todo/{ids}")
async def delete_todo(ids: int):
    try:
        obj = store_todo[ids]
        store_todo.pop(ids)
        return {"deleted todo": obj}
    except:
        raise HTTPException(status_code=400, detail="Todo not found for deleting")





