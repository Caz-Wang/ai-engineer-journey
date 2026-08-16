from api_client import get_post


def test_get_post():
    post = get_post(1)

    assert post is not None
    assert post["id"] == 1
    assert "title" in post
    assert "body" in post

def test_get_post_not_found():
    post = get_post(999999)

    assert post is None