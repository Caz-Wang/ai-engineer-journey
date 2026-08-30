import os

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://jsonplaceholder.typicode.com",
)

APP_NAME = os.getenv(
    "APP_NAME",
    "AI Engineer Journey",
)

MAX_RETRIES = int(
    os.getenv(
        "MAX_RETRIES",
        "3",
    )
)