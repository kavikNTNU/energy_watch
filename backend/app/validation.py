VALID_STATUSES = ("active", "inactive", "maintenance")
VALID_TYPES = ("meter", "battery", "charging_station", "transformator")
MAX_NAME_LENGTH = 100

def validate_component_data(data):
    errors = []

    # Validate name
    name = data.get("name")
    if not name or len(name) > MAX_NAME_LENGTH or not name.strip():
        errors.append(f"Name must be provided (only whitespaces is not allowed) and cannot exceed {MAX_NAME_LENGTH} characters.")

    # Validate status
    status = data.get("status")
    if status not in VALID_STATUSES:
        errors.append(f"Status must be one of {VALID_STATUSES}.")

    # Validate type
    component_type = data.get("type")
    if component_type not in VALID_TYPES:
        errors.append(f"Type must be one of {VALID_TYPES}.")

    return errors