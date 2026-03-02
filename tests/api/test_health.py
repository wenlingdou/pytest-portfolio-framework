import pytest


@pytest.mark.api
def test_status_200(api):
    resp = api.get("/status/200")
    assert resp.status_code == 200


