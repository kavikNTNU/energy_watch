from fastapi import FastAPI

app = FastAPI(title="Energy Watch API")


@app.get("/")
def read_root():
    return {"message": "Energy Watch API is running"}