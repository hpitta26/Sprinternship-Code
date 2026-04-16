
db = db.getSiblingDB("agentic_db")

db.items.insertMany([
    {
        "item_id": "item1",
        "content": "This is the content of item 1"
    },
    {
        "item_id": "item2",
        "content": "This is the content of item 2"
    }
])

print('Database initialized with items')