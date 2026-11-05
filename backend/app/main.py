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
async def create_component(request: Request):
    try:
        data = await request.json()
    except ValueError:
        raise HTTPException(status_code=400, detail="Request body must be valid JSON")

    if not isinstance(data, dict):
        raise HTTPException(status_code=400, detail="Request body must be a JSON object")

    errors = validate_component_data(data)
    if errors:
        raise HTTPException(status_code=400, detail=errors)

    component = repository.create_component(
        name=data["name"],
        status=data["status"],
        component_type=data["type"]
    )
    return component

@app.get("/api/components")
def list_components():
    return repository.list_components()

@app.get("/api/components/{component_id}")
def get_component(component_id: int):
    component = repository.get_component(component_id)
    if component is None:
        raise HTTPException(status_code=404, detail=f"Component {component_id} not found")
    return component

@app.put("/api/components/{component_id}")
async def update_component(component_id: int, request: Request):
    try:
        data = await request.json()
    except ValueError:
        raise HTTPException(status_code=400, detail="Request body must be valid JSON")

    if not isinstance(data, dict):
        raise HTTPException(status_code=400, detail="Request body must be a JSON object")

    errors = validate_component_data(data)
    if errors:
        raise HTTPException(status_code=400, detail=errors)

    component = repository.update_component(
        component_id=component_id,
        name=data["name"],
        status=data["status"],
        component_type=data["type"]
    )
    if component is None:
        raise HTTPException(status_code=404, detail=f"Component {component_id} not found")
    return component