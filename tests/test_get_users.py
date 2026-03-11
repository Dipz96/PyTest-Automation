import pytest
import math
from utils.assertions import assert_value,assert_key_present

@pytest.mark.smoke
def test_get_users(api_client):
    response = api_client.get("/users?page=2")
    body = response.json()

    assert_value(response.status_code,200,"status_code")
    #Top level Keys validation
    assert_key_present(body,["page","data"])

    #Type validations
    assert isinstance(body["page"], int)
    assert isinstance(body["data"], list)

    # Business validations
    assert_value(body["page"],2,"page")
    assert len(body["data"]) <= body["per_page"]

    expected_pages = math.ceil(body["total"] / body["per_page"])
    assert_value(body["total_pages"],expected_pages,"total_pages")

    # User schema validation
    user_ids = set()
    for user in body["data"]:
        assert_key_present(user,["id", "email", "first_name", "last_name", "avatar"])

        assert isinstance(user["id"], int)
        assert isinstance(user["email"], str)

        assert user["id"] not in user_ids
        user_ids.add(user["id"])

@pytest.mark.regression
def test_get_single_user(api_client,test_data):
    data=test_data["user_id"]
    id=data["valid_id"]["id"]
    email=data["expected_data"]["email"]
    response = api_client.get(f"/users/{id}")
    body=response.json()

    assert_key_present(body["data"],["id","email","first_name","last_name","avatar"])

    assert_value(response.status_code,200,"status_code")
    assert_value(body["data"]["id"],id,"id")
    assert_value(body["data"]["email"],email,"email")
    
