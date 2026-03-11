import pytest
from utils.assertions import assert_value,assert_key_present

@pytest.mark.dependency(name="register_user")
@pytest.mark.regression
def test_register_user(api_client,test_data):
    data  = test_data["register_user"]
    payload = data["valid_payload"]
    response = api_client.post("/register", json=payload)
    body=response.json()

    assert_key_present(body,["id","token"])
    assert_value(response.status_code,200,"status_code")
    assert_value(body["id"],data["expected_data"]["id"],"id")

    # store token for next tests
    data["expected_data"]["token"] = body["token"]


@pytest.mark.dependency(depends=["register_user"])
@pytest.mark.regression
def test_login_user(api_client,test_data):
    data  = test_data["register_user"]
    payload = data["valid_payload"]
    response = api_client.post("/login", json=payload)
    body=response.json()

    assert_key_present(body,["token"])
    assert_value(response.status_code,200,"status_code")
    assert_value(body["token"],data["expected_data"]["token"],"token")