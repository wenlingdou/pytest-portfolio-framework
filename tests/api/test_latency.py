import time

def test_latency(api):
    start = time.time()
    response = api.get("/status")
    end = time.time()
    latency = end - start

    print(f"Latency: {latency}")

    assert response.status_code == 200
    assert latency < 1.0   # 1 second threshold 
