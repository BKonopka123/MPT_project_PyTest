from utils.code import *
import pytest
import requests


class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}
    

@pytest.fixture
def mock_get(monkeypatch):
    def _mock_get(url):
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", _mock_get)


def test_get_json(mock_get):
    assert get_json("http://test.com") == {"mock_key": "mock_response"}