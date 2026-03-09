import pytest

@pytest.mark.api
def test_bearer_auth_without_token(api):
    resp = api.get("/bearer")
    assert resp.status_code == 401