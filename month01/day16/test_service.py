import pytest

from exceptions import PostNotFoundError
from models import Post
from service import PostService


class FakeRepository:
    def __init__(self, posts):
        self.posts = posts

    def get_posts(self, limit):
        return self.posts[:limit]


def test_get_post_returns_matching_post():
    posts = [
        Post(1, 1, "First Post", "First Body"),
        Post(1, 2, "Second Post", "Second Body"),
    ]

    service = PostService(FakeRepository(posts))

    post = service.get_post(2)

    assert post.id == 2
    assert post.title == "Second Post"


def test_get_post_raises_not_found_error():
    posts = [
        Post(1, 1, "First Post", "First Body"),
    ]

    service = PostService(FakeRepository(posts))

    with pytest.raises(PostNotFoundError, match="Post 99 was not found"):
        service.get_post(99)