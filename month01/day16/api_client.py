import requests

from config import API_BASE_URL
from exceptions import ApiError
from models import Post


def get_posts(limit: int) -> list[Post]:
    try:
        response = requests.get(
            f"{API_BASE_URL}/posts",
            timeout=5,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise ApiError(f"Failed to retrieve posts: {error}") from error

    data = response.json()

    return [
        Post(
            user_id=item["userId"],
            id=item["id"],
            title=item["title"],
            body=item["body"],
        )
        for item in data[:limit]
    ]