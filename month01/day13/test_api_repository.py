from api_repository import ApiPostRepository


def test_get_posts():
    repository = ApiPostRepository()

    posts = repository.get_posts(2)

    assert len(posts) == 2
    assert posts[0].id == 1
    assert posts[1].id == 2