import logging

import requests

from models import Post


def get_posts(limit: int = 5) -> list[Post]:
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

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

    except requests.RequestException as error:
        logging.error("Failed to retrieve posts: %s", error)
        return []