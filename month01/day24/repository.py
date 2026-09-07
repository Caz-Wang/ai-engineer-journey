from typing import Protocol

from models import Post


class PostRepository(Protocol):
    def get_posts(self, limit: int = 5) -> list[Post]:
        ...