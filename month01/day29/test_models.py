from models import Post, post_from_dict
import pytest

def test_create_post():
    post = Post(
        id=1,
        title="Test post",
        body="Test body",
    )

    assert post.id == 1
    assert post.title == "Test post"
    assert post.body == "Test body"

def test_post_repr():
    post = Post(
        id=1,
        title="Test post",
        body="Test body",
    )

    print(post)

def test_posts_are_equal():
    post1 = Post(
        id=1,
        title="Test post",
        body="Test body",
    )
    post2 = Post(
        id=1,
        title="Test post",
        body="Test body",
    )
    assert post1 == post2

def test_post_from_dict():
    data = {
        "id": 1,
        "title": "Test post",
        "body": "Test body",
    }

    post = post_from_dict(data)

    assert post.id == 1
    assert post.title == "Test post"
    assert post.body == "Test body"

def test_post_from_dict_missing_title():
    data = {
        "id": 1,
        "body": "Test body",
    }
    with pytest.raises(KeyError):
        post_from_dict(data)
