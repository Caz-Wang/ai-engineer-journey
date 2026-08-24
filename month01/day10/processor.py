from models import Post


def calculate_average_title_length(posts: list[Post]) -> float:
    if not posts:
        raise ValueError("posts cannot be empty")

    return sum(len(post.title) for post in posts) / len(posts)


def find_longest_title(posts: list[Post]) -> Post:
    if not posts:
        raise ValueError("posts cannot be empty")

    return max(posts, key=lambda post: len(post.title))


def create_summaries(posts: list[Post]) -> list[str]:
    return [post.summary() for post in posts]