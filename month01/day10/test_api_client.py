
from api_client import get_posts
from models import Post


def test_get_posts_success():
    posts = get_posts(3)

    assert len(posts) == 3
    assert all(isinstance(post, Post) for post in posts)


def test_get_posts_limit():
    posts = get_posts(1)

    assert len(posts) == 1
    assert posts[0].id == 1