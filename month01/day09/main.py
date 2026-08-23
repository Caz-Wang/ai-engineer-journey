import logging

from api_client import get_post


def main():
    logging.basicConfig(level=logging.INFO)

    post = get_post(1)

    if post is None:
        logging.error("Could not retrieve post")
        return

    logging.info("Retrieved post %d", post.id)
    logging.info("Title: %s", post.title)


if __name__ == "__main__":
    main()