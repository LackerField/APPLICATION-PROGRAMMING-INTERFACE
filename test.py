import requests

BASE_URL = "http://127.0.0.1:8000"

def test_api():
    print("=== Testing FastAPI Application ===")
    print("\n1. Testing GET /")
    print(requests.get(f"{BASE_URL}/").json())

    print("\n2. Testing GET /health")
    print(requests.get(f"{BASE_URL}/health").json())

    print("\n3. Testing POST /predict (Positive)")
    print(requests.post(f"{BASE_URL}/predict", json={"text": "I really enjoy building applications with FastAPI and Hugging Face!"}).json())

    print("\n4. Testing POST /predict (Negative)")
    print(requests.post(f"{BASE_URL}/predict", json={"text": "This lab assignment is completely frustrating and difficult."}).json())

    print("\n5. Testing POST /predict (Empty Input Error)")
    print(requests.post(f"{BASE_URL}/predict", json={"text": ""}).json())

if __name__ == "__main__":
    test_api()