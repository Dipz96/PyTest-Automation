import pytest
from utils.assertions import assert_value,assert_key_present

@pytest.mark.regression
def test_create_user(api_client, test_data):
    data  = test_data["create_user"]
    payload = data["invalid_payload_missing_name"]
    response = api_client.post("/users", json=payload)
    body=response.json()

    assert_key_present(body,["name","job","id","createdAt"])
    assert_value(response.status_code,data["expected_data"]["success"],"status_code")
    assert_value(body["name"],payload["name"],"name")
    assert_value(body["job"],payload["job"],"job")
