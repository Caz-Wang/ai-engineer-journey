from models import Post
from service import PostService


def fake_posts(limit: int) -> list[Post]:
    return [
        Post(1, 1, "First Post", "Hello"),
        Post(1, 2, "Second Post", "World"),
    ][:limit]


def test_get_posts():
    service = PostService(fake_posts)

    posts = service.get_posts(2)

    assert len(posts) == 2
    assert posts[0].title == "First Post"
    assert posts[1].title == "Second Post"


def test_get_summaries():
    service = PostService(fake_posts)

    summaries = service.get_summaries(2)

    assert summaries == [
        "Post 1: First Post",
        "Post 2: Second Post",
    ]


def test_get_posts_respects_limit():
    service = PostService(fake_posts)

    posts = service.get_posts(1)

    assert len(posts) == 1
    assert posts[0].id == 1