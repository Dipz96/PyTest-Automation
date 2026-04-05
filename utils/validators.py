import math
from utils.assertions import assert_value, assert_key_present
from utils.helpers import get_page


def validate_single_user(body, **kwargs):
    test_data=kwargs.get("test_data")
    data = test_data["user_id"]

    id = data["valid_id"]["id"]
    email = data["expected_data"]["email"]

    assert_key_present(body["data"], ["id","email","first_name","last_name","avatar"])

    assert_value(body["data"]["id"], id, "id")
    assert_value(body["data"]["email"], email, "email")


def validate_users_list(body, **kwargs):
    request=kwargs.get("request")
    assert_key_present(body, ["page", "data"])

    assert isinstance(body["page"], int)
    assert isinstance(body["data"], list)

    #get endpoint url using current request context
    endpoint=request.node._endpoint
    query_params=get_page(endpoint)

    #check if page exists in api url
    if "page" in query_params:
        expected_page = int(query_params["page"][0])
        assert_value(body["page"], expected_page, "page")

    assert len(body["data"]) <= body["per_page"]

    expected_pages = math.ceil(body["total"] / body["per_page"])
    assert_value(body["total_pages"], expected_pages, "total_pages")

    user_ids = set()

    for user in body["data"]:
        assert_key_present(user, ["id", "email", "first_name", "last_name", "avatar"])

        assert isinstance(user["id"], int)
        assert isinstance(user["email"], str)

        assert user["id"] not in user_ids
        user_ids.add(user["id"])


VALIDATION_MAP = {
    "single_user": validate_single_user,
    "users_list": validate_users_list,
}