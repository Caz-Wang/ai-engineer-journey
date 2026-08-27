from models import Post


class PostCache:
    def __init__(self):
        self._posts: dict[int, Post] = {}

    def get(self, post_id: int) -> Post | None:
        return self._posts.get(post_id)

    def set(self, post: Post) -> None:
        self._posts[post.id] = post

    def clear(self) -> None:
        self._posts.clear()