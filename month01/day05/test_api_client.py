from api_client import get_posts


def test_get_posts():
    posts = get_posts(3)

    assert len(posts) == 3
    assert posts[0]["id"] == 1
    assert posts[1]["id"] == 2
    assert posts[2]["id"] == 3


def test_get_posts_limit():
    posts = get_posts(5)

    assert len(posts) == 5
    