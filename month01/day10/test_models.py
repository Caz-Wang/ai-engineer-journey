import pytest

from models import Post


def test_post_creation():
    post = Post(1, 42, "Hello", "World")

    assert post.user_id == 1
    assert post.id == 42
    assert post.title == "Hello"
    assert post.body == "World"


def test_post_summary():
    post = Post(1, 42, "Hello AI", "Learning Python")

    assert post.summary() == "Post 42: Hello AI"


def test_empty_title_rejected():
    with pytest.raises(ValueError):
        Post(1, 1, "", "World")


def test_empty_body_rejected():
    with pytest.raises(ValueError):
        Post(1, 1, "Hello", "")