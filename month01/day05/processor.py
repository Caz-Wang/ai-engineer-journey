def calculate_average_title_length(posts: list) -> float:
    if not posts:
        return 0.0

    total_length = sum(len(post["title"]) for post in posts)

    return total_length / len(posts)


def find_longest_title(posts: list) -> dict | None:
    if not posts:
        return None

    return max(posts, key=lambda post: len(post["title"]))