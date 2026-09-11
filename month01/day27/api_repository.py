from api_client import get_posts
from models import Post


class ApiPostRepository:
    def get_posts(self, limit: int = 5) -> list[Post]:
        return get_posts(limit)