
import importlib


def test_default_config(monkeypatch):
    monkeypatch.delenv("API_BASE_URL", raising=False)
    monkeypatch.delenv("APP_NAME", raising=False)

    import config

    importlib.reload(config)

    assert config.API_BASE_URL == "https://jsonplaceholder.typicode.com"
    assert config.APP_NAME == "AI Engineer Journey"


def test_environment_variables_override_defaults(monkeypatch):
    monkeypatch.setenv("API_BASE_URL", "https://example.com/api")
    monkeypatch.setenv("APP_NAME", "Test AI App")

    import config

    importlib.reload(config)

    assert config.API_BASE_URL == "https://example.com/api"
    assert config.APP_NAME == "Test AI App"