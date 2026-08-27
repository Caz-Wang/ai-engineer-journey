import logging

from api_repository import ApiPostRepository
from service import PostService


def main():
    logging.basicConfig(level=logging.INFO)

    repository = ApiPostRepository()
    service = PostService(repository)

    post = service.get_post(1)

    if post is None:
        logging.error("Could not retrieve post")
        return

    logging.info("Retrieved post %d", post.id)
    logging.info("Title: %s", post.title)

    cached_post = service.get_post(1)

    if cached_post is not None:
        logging.info("Retrieved post %d from cache", cached_post.id)


if __name__ == "__main__":
    main()