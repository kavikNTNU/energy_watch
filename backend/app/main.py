from fastapi import FastAPI
from app.database import init_db

init_db()  # create the table if it doesn't exist

app = FastAPI(title="Energy Watch API")


@app.get("/")
def read_root():
    return {"message": "Energy Watch API is running"}