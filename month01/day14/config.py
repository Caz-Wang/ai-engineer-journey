import os

from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://jsonplaceholder.typicode.com",
)

APP_NAME = os.getenv(
    "APP_NAME",
    "AI Engineer Journey",
)