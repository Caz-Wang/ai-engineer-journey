from models import Post


class CountingRepository:
    def __init__(self):
        self.call_count = 0

    def get_posts(self, limit: int = 5) -> list[Post]:
        self.call_count += 1
        return [Post(1, 42, "Cached Post", "Testing cache")]