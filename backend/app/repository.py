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