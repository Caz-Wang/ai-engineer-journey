import logging

from api_repository import ApiPostRepository
from config import APP_NAME, API_BASE_URL
from service import PostService


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info("Application: %s", APP_NAME)
    logging.info("API Base URL: %s", API_BASE_URL)

    repository = ApiPostRepository()
    service = PostService(repository)

    post = service.get_post(1)

    if post is None:
        logging.error("Could not retrieve post")
        return

    logging.info("Retrieved post %d", post.id)
    logging.info("Title: %s", post.title)


if __name__ == "__main__":
    main()