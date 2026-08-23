from api_client import get_post
from models import Post


def test_get_post_success():
    post = get_post(1)

    assert isinstance(post, Post)
    assert post.id == 1
    assert post.title != ""


def test_get_post_not_found():
    post = get_post(999999)

    assert post is None


def test_get_post_invalid_id():
    post = get_post(0)

    assert post is None