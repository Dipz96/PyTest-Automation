# api/client.py

import requests

class APIClient:

    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        print(f"\n {method} {url}")
        print(f"Payload: {kwargs.get('json')}")

        response = requests.request(
            method,
            url,
            headers=self.headers,
            **kwargs
        )
        print(f"Response: {response.status_code}")
        return response