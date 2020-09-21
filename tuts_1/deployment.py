from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Package(BaseModel):
    name: str
    desc: Optional[str] = None
    body: List[str] = []


@app.post("/details/{ids}")
async def body_details(ids: int):
    return {"id": ids}
