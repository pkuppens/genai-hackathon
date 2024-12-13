from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
import databases
import sqlalchemy

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "mysql://myuser:mypassword@localhost/mydatabase")
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class Item(BaseModel):
    name: str
    description: str

items = []

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/items", response_model=List[Item])
async def get_items():
    query = "SELECT name, description FROM items"
    return await database.fetch_all(query)

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    query = "INSERT INTO items(name, description) VALUES (:name, :description)"
    await database.execute(query, values={"name": item.name, "description": item.description})
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    query = "UPDATE items SET name = :name, description = :description WHERE id = :item_id"
    await database.execute(query, values={"name": item.name, "description": item.description, "item_id": item_id})
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = "DELETE FROM items WHERE id = :item_id"
    await database.execute(query, values={"item_id": item_id})
    return {"message": "Item deleted successfully"}
