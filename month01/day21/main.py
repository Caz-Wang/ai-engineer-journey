import logging

from api_repository import ApiPostRepository
from config import APP_NAME
from exceptions import ApiError, PostNotFoundError
from service import PostService
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    logger.info("Application: %s", APP_NAME)

    repository = ApiPostRepository()
    service = PostService(repository)

    try:
        post = service.get_post(1)

        logger.info("Retrieved post %d", post.id)
        logger.info("Title: %s", post.title)

    except ApiError as error:
        logger.error("API error: %s", error)

    except PostNotFoundError as error:
        logger.error("Post error: %s", error)


if __name__ == "__main__":
    main()