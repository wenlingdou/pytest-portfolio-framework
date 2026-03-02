import requests

class APIClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str, **kwargs):
        url = f"{self.base_url}{path}"
        return requests.get(url, timeout=self.timeout, **kwargs)
    

    