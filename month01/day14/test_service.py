import time

from cache import PostCache
from counting_repository import CountingRepository
from service import PostService


def test_get_post_uses_cache():
    repository = CountingRepository()
    service = PostService(repository)

    first = service.get_post(42)
    second = service.get_post(42)

    assert first == second
    assert repository.call_count == 1


def test_get_post_fetches_again_after_cache_expires():
    repository = CountingRepository()
    cache = PostCache(ttl_seconds=0.1)
    service = PostService(repository, cache)

    service.get_post(42)

    time.sleep(0.2)

    service.get_post(42)

    assert repository.call_count == 2