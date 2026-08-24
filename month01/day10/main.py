import logging

from api_client import get_posts
from processor import calculate_average_title_length, create_summaries


def main():
    logging.basicConfig(level=logging.INFO)

    posts = get_posts(5)

    if not posts:
        logging.error("No posts were retrieved")
        return

    logging.info("Retrieved %d posts", len(posts))

    average_length = calculate_average_title_length(posts)
    logging.info("Average title length: %.2f", average_length)

    for summary in create_summaries(posts):
        logging.info(summary)


if __name__ == "__main__":
    main()