import logging

from api_repository import ApiPostRepository
from config import APP_NAME
from exceptions import ApiError, PostNotFoundError
from service import PostService


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info("Application: %s", APP_NAME)

    repository = ApiPostRepository()
    service = PostService(repository)

    try:
        post = service.get_post(1)

        logging.info("Retrieved post %d", post.id)
        logging.info("Title: %s", post.title)

    except ApiError as error:
        logging.error("API error: %s", error)

    except PostNotFoundError as error:
        logging.error("Post error: %s", error)


if __name__ == "__main__":
    main()