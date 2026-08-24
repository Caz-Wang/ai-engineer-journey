from config import API_BASE_URL, APP_NAME


def test_api_base_url():
    assert API_BASE_URL == "https://jsonplaceholder.typicode.com"


def test_app_name():
    assert APP_NAME == "AI Engineer Journey"