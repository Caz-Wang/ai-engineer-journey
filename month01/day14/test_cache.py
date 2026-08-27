import time

from cache import PostCache
from models import Post


def test_cache_miss():
    cache = PostCache()

    assert cache.get(1) is None


def test_cache_set_and_get():
    cache = PostCache()
    post = Post(1, 42, "Hello", "World")

    cache.set(post)

    assert cache.get(42) == post


def test_cache_clear():
    cache = PostCache()
    post = Post(1, 42, "Hello", "World")

    cache.set(post)
    cache.clear()

    assert cache.get(42) is None


def test_cache_expires():
    cache = PostCache(ttl_seconds=0.1)
    post = Post(1, 42, "Hello", "World")

    cache.set(post)

    time.sleep(0.2)

    assert cache.get(42) is None