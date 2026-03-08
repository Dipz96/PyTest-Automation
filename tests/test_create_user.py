import pytest
from utils.assertions import assert_status_code

@pytest.mark.regression
def test_create_user(api_client, test_data):
    data  = test_data["create_user"]
    payload = data["valid_payload"]
    response = api_client.post("/users", json=payload)

    assert_status_code(response,200)
    assert response.json()["name"] == payload["name"]