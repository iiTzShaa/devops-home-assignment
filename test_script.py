import requests

# Define the URLs and expected status codes for each endpoint
servers = [
    {"url": "http://nginx:8080", "expected_status": 200},
    {"url": "http://nginx:8081", "expected_status": 500},
]

# Send a GET request to a server and check the status code

def check_server(server):
    try:
        response = requests.get(server["url"])
        if response.status_code == server["expected_status"]:
            print(f"SUCCESS: {server['url']} responded with {server['expected_status']}")
        else:
            print(f"FAIL: {server['url']} responded with {response.status_code}, expected {server['expected_status']}")
            return False
    except Exception as e:
        print(f"ERROR: Could not reach {server['url']}. Exception: {e}")
        return False
    return True

if __name__ == "__main__":
    all_tests_passed = all(check_server(server) for server in servers)
    if all_tests_passed:
        print("All tests passed successfully.")
    else:
        print("Some tests failed.")
    exit(0 if all_tests_passed else 1)