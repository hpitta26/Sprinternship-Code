import os

from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
MONGO_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=5000)
db = client.agentic_db


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item = await db.items.find_one({"item_id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item["_id"] = str(item["_id"])
    return item


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
