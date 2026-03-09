import pytest


@pytest.mark.api 
def test_bearer_auth(api):

    headers = {
        "Authorization": "Bearer demo_token"
    }

    resp = api.get("/bearer", headers=headers)

    assert resp.status_code == 200
    