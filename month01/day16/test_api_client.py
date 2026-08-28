import pytest
import requests

from api_client import get_posts
from exceptions import ApiError


def test_get_posts_returns_posts(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return [
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Test Post",
                    "body": "Test Body",
                }
            ]

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    posts = get_posts(1)

    assert len(posts) == 1
    assert posts[0].id == 1
    assert posts[0].title == "Test Post"


def test_get_posts_raises_api_error(monkeypatch):
    def fake_get(*args, **kwargs):
        raise requests.RequestException("Network failure")

    monkeypatch.setattr(requests, "get", fake_get)

    with pytest.raises(ApiError, match="Failed to retrieve posts"):
        get_posts(1)