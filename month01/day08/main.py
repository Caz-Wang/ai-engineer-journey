import logging

from api_client import get_posts


def main():
    logging.basicConfig(level=logging.INFO)

    posts = get_posts(5)

    logging.info("Retrieved %d posts", len(posts))

    for post in posts:
        logging.info("Post %d: %s", post.id, post.title)


if __name__ == "__main__":
    main()