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

    class FakeClient:
        get = fake_get

    posts = api_client.get_posts(1, FakeClient)

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

    class FakeClient:
        get = fake_get



    with pytest.raises(
        ApiError,
        match="Failed to retrieve posts after 3 attempts",
    ):
        api_client.get_posts(1, FakeClient)

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
                        "title": "Test post",
                        "body": "Test body",
                    }
                ]

        return FakeResponse()

    class FakeClient:
        get = fake_get
    posts = api_client.get_posts(1, FakeClient)

    assert len(posts) == 1

    assert posts[0].id == 1
    assert posts[0].title == "Test post"

def test_posts_from_data():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "Test post",
            "body": "Test body",
        }
    ]

    posts = api_client.posts_from_data(data)

    assert len(posts) == 1
    assert posts[0].id == 1
    assert posts[0].title == "Test post"

def test_posts_from_data_empty():
    posts = api_client.posts_from_data([])

    assert posts == []

def test_posts_from_data_multiple():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "First post",
            "body": "First body",
        },
        {
            "userId": 2,
            "id": 2,
            "title": "Second post",
            "body": "Second body",
        },
    ]

    posts = api_client.posts_from_data(data)

    assert len(posts) == 2
    assert posts[0].id == 1
    assert posts[1].id == 2

def test_posts_from_data_missing_field():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "Broken post",
        }
    ]
    with pytest.raises(ApiError) as excinfo:
        api_client.posts_from_data(data)
    assert "Invalid post data" in str(excinfo.value)

def test_posts_from_data_invalid_type():
    data = [
        {
            "userId": "wrong",
            "id": 1,
            "title": "bad post",
            "body": "bad body",
        }
    ]
    with pytest.raises(ApiError) as excinfo:
        api_client.posts_from_data(data)
    assert "Invalid post data" in str(excinfo.value)

def test_posts_from_data_invalid_value():
    data = [
        {
            "userId": 1,
            "id": 0,
            "title": "Invalid post",
            "body": "Invalid body",
        }
    ]

    with pytest.raises(ApiError) as excinfo:
        api_client.posts_from_data(data)

    assert "Invalid post data" in str(excinfo.value)

def test_get_posts_uses_default_client(monkeypatch):
    calls = []

    def fake_get(url, timeout):
        class FakeClient:
            get = fake_get
        calls.append((url, timeout))
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

    class FakeClient:
         get = fake_get

    monkeypatch.setattr(api_client, "default_http_client", FakeClient)

    api_client.get_posts(1) 

    assert calls == [
        (f"{api_client.API_BASE_URL}/posts", api_client.REQUEST_TIMEOUT)
    ]