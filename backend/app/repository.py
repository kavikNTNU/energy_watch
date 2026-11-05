from datetime import datetime, timezone
from app.database import get_connection

def now() -> str:
    return datetime.now(timezone.utc).isoformat()

def create_component(name: str, status: str, component_type: str) -> dict:
    last_updated = now()
    connection = get_connection()
    try:
        cursor = connection.execute(
            "INSERT INTO components (name, status, type, last_updated) VALUES (?, ?, ?, ?)",
            (name, status, component_type, now())
        )
        connection.commit()
    finally:
        connection.close()

    return {
        "id": cursor.lastrowid,
        "name": name,
        "status": status,
        "type": component_type,
        "lastUpdated": last_updated,
    }

def _to_dict(row) -> dict:
    return {
        "id": row["id"],
        "name": row["name"],
        "status": row["status"],
        "type": row["type"],
        "lastUpdated": row["last_updated"],
    }

def list_components() -> list:
    connection = get_connection()
    try:
        rows = connection.execute("SELECT * FROM components").fetchall()
    finally:
        connection.close()

    return [_to_dict(row) for row in rows]

def get_component(component_id: int) -> dict | None:
    connection = get_connection()
    try:
        row = connection.execute("SELECT * FROM components WHERE id = ?", (component_id,)).fetchone()
    finally:
        connection.close()

    return _to_dict(row) if row else None