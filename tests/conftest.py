import pytest
from src.core.api_client import APIClient
from src.core.config import BASE_URL, TIMEOUT


@pytest.fixture(scope="session")
def api():
    """
    Session-level API client fixture.
    Created once per test session.
    """
    return APIClient(BASE_URL, timeout=TIMEOUT)

