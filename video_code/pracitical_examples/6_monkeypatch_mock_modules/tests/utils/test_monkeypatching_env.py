import pytest
from utils.code import *


@pytest.fixture
def mock_env_user(monkeypatch):
    monkeypatch.setenv("USER", "TEST")


@pytest.fixture
def mock_env_missing(monkeypatch):
    monkeypatch.delenv("USER", raising=False)


def test_get_os_user_lower(mock_env_user):
    assert get_os_user_lower() == "test"


def test_raise_get_os_user_lower(mock_env_missing):
    with pytest.raises(ValueError):
        _ = get_os_user_lower()