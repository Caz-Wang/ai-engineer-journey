from counting_repository import CountingRepository
from service import PostService


def test_get_post_uses_cache():
    repository = CountingRepository()
    service = PostService(repository)

    first = service.get_post(42)
    second = service.get_post(42)

    assert first == second
    assert repository.call_count == 1


def test_get_post_returns_post():
    repository = CountingRepository()
    service = PostService(repository)

    post = service.get_post(42)

    assert post is not None
    assert post.id == 42
    assert post.title == "Cached Post"