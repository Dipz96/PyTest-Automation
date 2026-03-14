import pytest
from utils.assertions import assert_value,assert_updationTime

@pytest.mark.regression
def test_update_user(api_client,test_data):
    data  = test_data["update_user"]
    payload = data["valid_payload"]
    id=payload["id"]
    response = api_client.put(f"/users/{id}", json=payload)
    body=response.json()

    assert_value(response.status_code,200,"status_code")
    assert_value(body["id"],data["expected_data"]["id"],"id")
    assert_value(body["email"],data["expected_data"]["email"],"email")
    assert_value(body["password"],data["expected_data"]["password"],"password")
    assert_updationTime(body["updatedAt"])

@pytest.mark.smoke
@pytest.mark.regression
def test_partialupdate_user(api_client,test_data):
    data  = test_data["partialupdate_user"]
    payload = data["valid_payload"]
    id=payload["id"]
    response = api_client.put(f"/users/{id}", json=payload)
    body=response.json()

    assert_value(response.status_code,200,"status_code")
    assert_value(body["id"],data["expected_data"]["id"],"id")
    assert_value(body["name"],data["expected_data"]["name"],"name")
    assert_updationTime(body["updatedAt"])
