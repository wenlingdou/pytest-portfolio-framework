import pytest

@pytest.mark.api
@pytest.mark.parametrize("code", [200, 201, 204, 400, 404])
def test_status_codes(api, code):

    resp = api.get(f"/status/{code}")
    assert resp.status_code == code

    