import requests
from concurrent.futures import ThreadPoolExecutor
from collections import Counter

from seed_stock import seed_stock

URL = "http://127.0.0.1:8000/api/purchase/"


def make_purchase():
    try:
        return requests.post(URL, json={"product_id": 1}).status_code
    except Exception as exc:
        print("Request error:", exc)
        return None


def run_test(total_requests=100, max_workers=50):
    seed_stock(stock=50)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(make_purchase) for _ in range(total_requests)]
        results = [future.result() for future in futures]

    counts = Counter(results)

    successful = counts.get(200, 0)
    failed = total_requests - successful

    print("\n=== TEST RESULT ===")
    print("Total Requests :", total_requests)
    print("Successful     :", successful)
    print("Failed         :", failed)


if __name__ == "__main__":
    run_test()