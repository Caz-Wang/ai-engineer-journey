from exceptions import PostNotFoundError
from repository import PostRepository


class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def get_post(self, post_id: int):
        posts = self.repository.get_posts(100)

        for post in posts:
            if post.id == post_id:
                return post

        raise PostNotFoundError(f"Post {post_id} was not found")