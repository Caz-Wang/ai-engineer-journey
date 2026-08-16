import logging

from api_client import get_posts
from processor import calculate_average_title_length, find_longest_title


def main():
    logging.basicConfig(level=logging.INFO)

    posts = get_posts(5)

    logging.info("Retrieved %d posts", len(posts))

    average_length = calculate_average_title_length(posts)
    longest_title = find_longest_title(posts)

    logging.info("Average title length: %.2f", average_length)

    if longest_title:
        logging.info("Longest title belongs to post %d", longest_title["id"])


if __name__ == "__main__":
    main()
    