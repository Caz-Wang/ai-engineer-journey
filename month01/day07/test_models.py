from models import Post


def test_post_creation():
    post = Post(
        user_id=1,
        id=1,
        title="Hello",
        body="World",
    )

    assert post.user_id == 1
    assert post.id == 1
    assert post.title == "Hello"
    assert post.body == "World"