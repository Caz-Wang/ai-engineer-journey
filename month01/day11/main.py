import logging

from config import APP_NAME
from service import PostService


def main():
    logging.basicConfig(level=logging.INFO)

    service = PostService()
    summaries = service.get_summaries(5)

    logging.info("Application: %s", APP_NAME)
    logging.info("Retrieved %d posts", len(summaries))

    for summary in summaries:
        logging.info(summary)


if __name__ == "__main__":
    main()