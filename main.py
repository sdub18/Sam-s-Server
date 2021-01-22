from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# Main Route
@app.get("/")
async def root():
    return {"message": "Hello World"}