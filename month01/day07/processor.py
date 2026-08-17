from models import Post


def calculate_average_title_length(posts: list[Post]) -> float:
    if not posts:
        return 0.0

    total_length = sum(len(post.title) for post in posts)

    return total_length / len(posts)


def find_longest_title(posts: list[Post]) -> Post | None:
    if not posts:
        return None

    return max(posts, key=lambda post: len(post.title))