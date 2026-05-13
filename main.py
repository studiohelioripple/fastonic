from fastapi import FastAPI

from db import init_db
from routes import router

app = FastAPI(
    title="ParsPack FastAPI Example",
    version="1.0.0"
)


init_db()
# app.include_router(router)


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}
