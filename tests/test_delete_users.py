import pytest
from utils.assertions import assert_value,assert_updationTime

def test_delete_user(api_client,test_data):
    data  = test_data["delete_user"]
    id = data["valid_payload"]["id"]
    response = api_client.delete(f"/users/{id}")

    assert_value(response.status_code,data["expected_data"]["status_code"],"status_code")
   