import logging

import requests

from models import Post


def get_post(post_id: int) -> Post | None:
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        return Post(
            user_id=data["userId"],
            id=data["id"],
            title=data["title"],
            body=data["body"],
        )

    except requests.RequestException as error:
        logging.error("Failed to retrieve post %d: %s", post_id, error)
        return None