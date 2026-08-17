from models import Post
from processor import calculate_average_title_length, find_longest_title


def test_calculate_average_title_length():
    posts = [
        Post(1, 1, "Hello", "World"),
        Post(1, 2, "Python", "Programming"),
    ]

    result = calculate_average_title_length(posts)

    assert result == 5.5


def test_calculate_average_title_length_empty():
    assert calculate_average_title_length([]) == 0.0


def test_find_longest_title():
    posts = [
        Post(1, 1, "Short", "A"),
        Post(1, 2, "This is longer", "B"),
    ]

    result = find_longest_title(posts)

    assert result.id == 2


def test_find_longest_title_empty():
    assert find_longest_title([]) is None