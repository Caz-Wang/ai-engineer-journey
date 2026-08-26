from models import Post


class FakePostRepository:
    def __init__(self):
        self.posts = [
            Post(1, 1, "First Post", "Hello"),
            Post(1, 2, "Second Post", "World"),
            Post(1, 3, "Third Post", "Testing"),
        ]

    def get_posts(self, limit: int = 5) -> list[Post]:
        return self.posts[:limit]