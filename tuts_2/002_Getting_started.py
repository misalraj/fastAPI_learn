from fastapi import FastAPI
# import uvicorn

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"name": "Misal"}


# if __name__ == "__main__":
#     uvicorn.run(app)
