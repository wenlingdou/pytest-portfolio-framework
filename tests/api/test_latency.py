import time
import pytest

@pytest.mark.api
def test_latency(api):
    start = time.time()
    response = api.get("/status/200")  # because the endpoint "/status/200" passed in test_health
    end = time.time()
    latency = end - start

    print(f"Latency: {latency}")

    assert response.status_code == 200
    assert latency < 1.0   # 1 second threshold 
