import logging
import pytest
import requests
import importlib

import config

import api_client
from exceptions import ApiError


def test_get_posts_retries_then_succeeds(monkeypatch):
    attempts = {"count": 0}
    delays = []

    def fake_sleep(seconds):
        delays.append(seconds)
        logging.info("Fake sleep called for %s seconds", seconds)

    monkeypatch.setattr(api_client.time, "sleep", fake_sleep)
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return [
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Retry Success",
                    "body": "Worked after retries",
                }
            ]

    def fake_get(*args, **kwargs):
        attempts["count"] += 1

        if attempts["count"] < 3:
            raise requests.RequestException("Temporary failure")

        return FakeResponse()

    monkeypatch.setattr(api_client.requests, "get", fake_get)

    posts = api_client.get_posts(1)

    assert len(posts) == 1
    assert posts[0].title == "Retry Success"
    assert attempts["count"] == 3
    assert delays == [1, 1]


def test_get_posts_raises_api_error_after_all_retries(monkeypatch):
    attempts = {"count": 0}
    delays = []
    def fake_sleep(seconds):
        delays.append(seconds)
    monkeypatch.setattr(api_client.time, "sleep", fake_sleep)
    def fake_get(*args, **kwargs):
        attempts["count"] += 1
        raise requests.RequestException("Network failure")

    monkeypatch.setattr(api_client.requests, "get", fake_get)

    with pytest.raises(
        ApiError,
        match="Failed to retrieve posts after 3 attempts",
    ):
        api_client.get_posts(1)

    assert attempts["count"] == 3
    assert delays == [1, 1]

def test_get_posts_uses_configured_timeout_from_environment(monkeypatch):
    monkeypatch.setenv("REQUEST_TIMEOUT", "10")

    importlib.reload(config)
    importlib.reload(api_client)

    received = {}

    def fake_get(*args, **kwargs):
        received["timeout"] = kwargs["timeout"]

        class FakeResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return [
                    {
                        "userId": 1,
                        "id": 1,
                        "title": "Test",
                        "body": "Test body",
                    }
                ]

        return FakeResponse()

    monkeypatch.setattr(api_client.requests, "get", fake_get)

    api_client.get_posts(1)

    assert received["timeout"] == 10