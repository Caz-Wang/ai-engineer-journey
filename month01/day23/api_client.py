
import logging
import time

import requests


from config import API_BASE_URL, MAX_RETRIES, RETRY_DELAY,REQUEST_TIMEOUT
from exceptions import ApiError
from models import Post
from typing import TypedDict

logger = logging.getLogger(__name__)

class PostData(TypedDict):
    userId: int
    id: int
    title: str
    body: str

def posts_from_data(data: list[PostData]) -> list[Post]:
    posts = []

    for item in data:
        try:
            post = Post(
                user_id=item["userId"],
                id=item["id"],
                title=item["title"],
                body=item["body"],
            )
            posts.append(post)

        except KeyError as error:
            raise ApiError(f"Invalid post data: missing field {error}")
        except TypeError as error:
            raise ApiError(f"Invalid post data: wrong type {error}")
        except ValueError as error:
            raise ApiError(f"Invalid post data: invalid value {error}")
        
    return posts



def get_posts(limit: int) -> list[Post]:
    
    logger.debug("Fetching posts with limit=%d", limit)

    
    last_error = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info(
                "API request attempt %d of %d",
                attempt,
                MAX_RETRIES,
            )

            response = requests.get(
                f"{API_BASE_URL}/posts",
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()

            data = response.json()

            return posts_from_data(data[:limit])

        
        except requests.RequestException as error:
            last_error = error

            logger.warning(
                "API request attempt %d failed: %s",
                attempt,
                error,
            )

            if attempt < MAX_RETRIES:
                logger.info("Retrying in %d seconds...", RETRY_DELAY)
                time.sleep(RETRY_DELAY)

    raise ApiError(
        f"Failed to retrieve posts after {MAX_RETRIES} attempts: {last_error}"
    )