import pytest

from models import Post
from processor import (
    calculate_average_title_length,
    create_summaries,
    find_longest_title,
)


def make_posts():
    return [
        Post(1, 1, "Hello", "World"),
        Post(1, 2, "Longer Title", "World"),
        Post(1, 3, "Hi", "World"),
    ]


def test_average_title_length():
    posts = make_posts()

    assert calculate_average_title_length(posts) == pytest.approx(19 / 3)


def test_find_longest_title():
    posts = make_posts()

    result = find_longest_title(posts)

    assert result.id == 2
    assert result.title == "Longer Title"


def test_create_summaries():
    posts = make_posts()

    assert create_summaries(posts) == [
        "Post 1: Hello",
        "Post 2: Longer Title",
        "Post 3: Hi",
    ]


def test_average_title_length_empty():
    with pytest.raises(ValueError):
        calculate_average_title_length([])


def test_find_longest_title_empty():
    with pytest.raises(ValueError):
        find_longest_title([])