from config import APP_NAME, APP_ENV


def test_app_name():
    assert APP_NAME == "AI Engineer Journey"


def test_app_env():
    assert APP_ENV == "development"