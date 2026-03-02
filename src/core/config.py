import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://httpbin.org").rstrip("/")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))

