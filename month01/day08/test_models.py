import pytest

from models import Post


def test_post_creation():
    post = Post(1, 1, "Hello", "World")

    assert post.user_id == 1
    assert post.id == 1
    assert post.title == "Hello"
    assert post.body == "World"


def test_post_to_dict():
    post = Post(1, 1, "Hello", "World")

    assert post.to_dict() == {
        "user_id": 1,
        "id": 1,
        "title": "Hello",
        "body": "World",
    }


def test_post_to_json():
    post = Post(1, 1, "Hello", "World")

    assert post.to_json() == (
        '{"user_id": 1, "id": 1, "title": "Hello", "body": "World"}'
    )


def test_empty_title_rejected():
    with pytest.raises(ValueError, match="title cannot be empty"):
        Post(1, 1, "", "World")


def test_empty_body_rejected():
    with pytest.raises(ValueError, match="body cannot be empty"):
        Post(1, 1, "Hello", "")


def test_invalid_user_id_rejected():
    with pytest.raises(ValueError, match="user_id must be positive"):
        Post(0, 1, "Hello", "World")


def test_invalid_post_id_rejected():
    with pytest.raises(ValueError, match="id must be positive"):
        Post(1, 0, "Hello", "World")