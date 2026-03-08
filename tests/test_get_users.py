import pytest
import math
from utils.assertions import assert_status_code

@pytest.mark.smoke
def test_get_users(api_client):
    response = api_client.get("/users?page=2")
    body = response.json()

    assert_status_code(response,200)
    #Top level Keys validation
    assert "page" in body
    assert "data" in body
    assert "data" in body
    #Type validations
    assert isinstance(body["page"], int)
    assert isinstance(body["data"], list)

    # Business validations
    assert body["page"] == 2
    assert len(body["data"]) <= body["per_page"]

    expected_pages = math.ceil(body["total"] / body["per_page"])
    assert body["total_pages"] == expected_pages

    # User schema validation
    user_ids = set()
    for user in body["data"]:
        for field in ["id", "email", "first_name", "last_name", "avatar"]:
            assert field in user

        assert isinstance(user["id"], int)
        assert isinstance(user["email"], str)

        assert user["id"] not in user_ids
        user_ids.add(user["id"])