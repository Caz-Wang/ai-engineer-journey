from repository import PostRepository


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def get_posts(self, limit: int = 5):
        return self.repository.get_posts(limit)

    def get_summaries(self, limit: int = 5) -> list[str]:
        posts = self.get_posts(limit)
        return [post.summary() for post in posts]