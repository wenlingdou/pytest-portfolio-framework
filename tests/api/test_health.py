import pytest


@pytest.mark.smoke

def test_status_200(api):
    resp = api.get("/status/200")
    assert resp.status_code == 200





