from unittest.mock import Mock

import api_client
from models import Post

def test_get_posts_returns_post_objects():
    response = Mock()
    response.json.return_value = [
        {
            "id": 1,
            "title": "Test post",
            "body": "Test body",
        }
    ]
    response.raise_for_status.return_value = None
    client = Mock()
    client.get.return_value = response
    posts = api_client.get_posts(1, client)
    assert isinstance(posts[0], Post)
    assert posts[0].id == 1
    assert posts[0].title == "Test post"
    assert posts[0].body == "Test body"