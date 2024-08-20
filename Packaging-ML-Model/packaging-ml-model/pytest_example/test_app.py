import pytest
import requests

def test_app():
    url = 'http://localhost:5001'
    try:
        response = requests.get(url, timeout=10)
        assert response.status_code == 200
        assert response.text == 'Hello, Pytest!'
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request error when connect to {url}: {e}")
