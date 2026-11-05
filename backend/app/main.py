from fastapi import FastAPI, HTTPException, Request
from app.database import init_db
from app import repository
from app.validation import validate_component_data

init_db()  # create the table if it doesn't exist

app = FastAPI(title="Energy Watch API")


@app.get("/")
def read_root():
    return {"message": "Energy Watch API is running"}

@app.post("/api/components", status_code=201)
def create_component(request: Request):
    data = request.json()
    errors = validate_component_data(data)
    if errors:
        raise HTTPException(status_code=400, detail=errors)

    component = repository.create_component(
        name=data["name"],
        status=data["status"],
        component_type=data["type"]
    )
    return component