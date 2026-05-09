from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

# Example API endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id,
     
    }
