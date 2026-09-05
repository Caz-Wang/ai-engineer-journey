
import logging
import time

import requests
logger = logging.getLogger(__name__)

from config import API_BASE_URL, MAX_RETRIES, RETRY_DELAY,REQUEST_TIMEOUT
from exceptions import ApiError
from models import Post


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

            return [
                Post(
                    user_id=item["userId"],
                    id=item["id"],
                    title=item["title"],
                    body=item["body"],
                )
                for item in data[:limit]
            ]

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