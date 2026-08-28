import time

from models import Post


class PostCache:
    def __init__(self, ttl_seconds: float = 60):
        self.ttl_seconds = ttl_seconds
        self._posts: dict[int, tuple[Post, float]] = {}

    def get(self, post_id: int) -> Post | None:
        cached = self._posts.get(post_id)

        if cached is None:
            return None

        post, stored_time = cached

        current_time = time.time()

        if current_time - stored_time > self.ttl_seconds:
            del self._posts[post_id]
            return None

        return post

    def set(self, post: Post) -> None:
        self._posts[post.id] = (post, time.time())

    def clear(self) -> None:
        self._posts.clear()