import logging

from api_repository import ApiPostRepository
from service import PostService


def main():
    logging.basicConfig(level=logging.INFO)

    repository = ApiPostRepository()
    service = PostService(repository)

    summaries = service.get_summaries(5)

    logging.info("Retrieved %d posts", len(summaries))

    for summary in summaries:
        logging.info(summary)


if __name__ == "__main__":
    main()