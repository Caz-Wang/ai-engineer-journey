import os

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://jsonplaceholder.typicode.com",
)

APP_NAME = os.getenv(
    "APP_NAME",
    "AI Engineer Journey",
)
def get_int_config(value, name):
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(f"{name} must be an integer")


def validate_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def validate_non_negative(value, name):
    if value < 0:
        raise ValueError(f"{name} must be a non-negative integer")
    return value
MAX_RETRIES = validate_positive(
    get_int_config(
        os.getenv(
            "MAX_RETRIES",
            "3",
        ),
        "MAX_RETRIES",
    ),
    "MAX_RETRIES",
)

REQUEST_TIMEOUT = validate_positive(
    get_int_config(
        os.getenv(
            "REQUEST_TIMEOUT",
            "5",
        ),
        "REQUEST_TIMEOUT",
    ),
    "REQUEST_TIMEOUT",
)

RETRY_DELAY = validate_non_negative(
    get_int_config(
        os.getenv(
            "RETRY_DELAY",
            "1",
        ),
        "RETRY_DELAY",
    ),
    "RETRY_DELAY",
)