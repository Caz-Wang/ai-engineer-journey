import importlib

import pytest

import config

def test_max_retries_must_be_positive(monkeypatch):
    monkeypatch.setenv("MAX_RETRIES", "-1")
    with pytest.raises(ValueError) as excinfo:
        importlib.reload(config)
    assert "MAX_RETRIES must be a positive integer" in str(excinfo.value)

def test_request_timeout_must_be_positive(monkeypatch):
    monkeypatch.setenv("REQUEST_TIMEOUT", "-1")
    with pytest.raises(ValueError) as excinfo:
        importlib.reload(config)
    assert "REQUEST_TIMEOUT must be a positive integer" in str(excinfo.value)

def test_retry_delay_must_be_non_negative(monkeypatch):
    monkeypatch.setenv("RETRY_DELAY", "-1")
    with pytest.raises(ValueError) as excinfo:
        importlib.reload(config)
    assert "RETRY_DELAY must be a non-negative integer" in str(excinfo.value)

def test_retry_delay_zero_is_allowed(monkeypatch):
    monkeypatch.setenv("RETRY_DELAY", "0")
    importlib.reload(config)
    assert config.RETRY_DELAY == 0

def test_invalid_integer_config(monkeypatch):
    monkeypatch.setenv("MAX_RETRIES", "banana")
    with pytest.raises(ValueError) as excinfo:
        importlib.reload(config)
    assert "MAX_RETRIES must be an integer" in str(excinfo.value)