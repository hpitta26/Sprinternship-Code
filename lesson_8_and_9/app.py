import os

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
MONGO_URL = os.getenv("MONGODB_URL", "mongodb://host.docker.internal:27017")
print(f'Using MongoDB URL: {MONGO_URL}')
client = AsyncIOMotorClient(MONGO_URL)
db = client.agentic_db


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item = await db.items.find_one({"item_id": item_id})
    if not item:
        raise {"error": "Item not found"}
    item["_id"] = str(item["_id"])
    return item


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
