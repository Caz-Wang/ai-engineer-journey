import os

from dotenv import load_dotenv


load_dotenv()


APP_NAME = os.getenv("APP_NAME")
APP_ENV = os.getenv("APP_ENV")


if not APP_NAME:
    raise ValueError("APP_NAME is required")

if not APP_ENV:
    raise ValueError("APP_ENV is required")