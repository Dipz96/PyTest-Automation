import pytest
from utils.assertions import assert_value,assert_key_present

def test_update_user(api_client,test_data):
    data  = test_data["register_user"]
    payload = data["valid_payload"]
    response = api_client.post("/register", json=payload)
    body=response.json()

    assert_key_present(body,["id","token"])
    assert_value(response.status_code,200,"status_code")
    assert_value(body["id"],data["expected_data"]["id"],"id")

    # store token for next tests
    data["expected_data"]["token"] = body["token"]