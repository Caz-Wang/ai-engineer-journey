from cache import PostCache
from repository import PostRepository


class PostService:
    def __init__(
        self,
        repository: PostRepository,
        cache: PostCache | None = None,
    ):
        self.repository = repository
        self.cache = cache or PostCache()

    def get_post(self, post_id: int):
        cached = self.cache.get(post_id)

        if cached is not None:
            return cached

        posts = self.repository.get_posts(post_id)

        if not posts:
            return None

        post = posts[0]
        self.cache.set(post)
        return post

    def get_summaries(self, limit: int = 5) -> list[str]:
        posts = self.repository.get_posts(limit)
        return [post.summary() for post in posts]