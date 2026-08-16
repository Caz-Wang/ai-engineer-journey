import requests


def get_posts(limit: int) -> list:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=5
    )

    response.raise_for_status()

    posts = response.json()

    return posts[:limit]
