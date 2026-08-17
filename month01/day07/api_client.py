import requests

from models import Post


def get_posts(limit: int) -> list[Post]:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=5,
    )

    response.raise_for_status()

    data = response.json()

    return [
        Post(
            user_id=post["userId"],
            id=post["id"],
            title=post["title"],
            body=post["body"],
        )
        for post in data[:limit]
    ]
