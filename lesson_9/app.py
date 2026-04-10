from fastapi import FastAPI

# http://localhost:<port>/docs#/ --> view the Swagger UI API documentation

app = FastAPI()

@app.get('/') # decorator --> middleware that wraps the function (executes before the function)
def read_root():
    return {"message": "Hello, World!"}

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get('/users/{user_id}')
def read_user(user_id: int):
    return {"user_id": user_id}