from collections.abc import Callable

from api_client import get_posts
from models import Post


class PostService:
    def __init__(
        self,
        post_provider: Callable[[int], list[Post]] = get_posts,
    ):
        self.post_provider = post_provider

    def get_posts(self, limit: int = 5) -> list[Post]:
        return self.post_provider(limit)

    def get_summaries(self, limit: int = 5) -> list[str]:
        posts = self.get_posts(limit)
        return [post.summary() for post in posts]