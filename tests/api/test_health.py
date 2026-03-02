import pytest
from src.core.api_client import APIClient
from src.core.config import BASE_URL, TIMEOUT

@pytest.mark.api
def test_status_200():
    api = APIClient(BASE_URL, timeout=TIMEOUT)
    resp = api.get("/status/200")
    assert resp.status_code == 200

    