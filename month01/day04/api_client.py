import requests


def get_post(post_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        timeout=5
    )

    try:
        response.raise_for_status()
    except requests.HTTPError:
        return None

    return response.json()