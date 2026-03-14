import pytest
import math
from utils.assertions import assert_value,assert_key_present

@pytest.mark.regression
def test_get_resources(api_client,test_data):
    data=test_data["resource_id"]
    response = api_client.get("/unknown")
    body = response.json()

    assert_value(response.status_code,data["expected_data"]["success"],"status_code")
    #Top level Keys validation
    assert_key_present(body,["page","data"])

    #Type validations
    assert isinstance(body["page"], int)
    assert isinstance(body["data"], list)

    # Business validations
    assert_value(body["page"],1,"page")
    assert len(body["data"]) <= body["per_page"]

    expected_pages = math.ceil(body["total"] / body["per_page"])
    assert_value(body["total_pages"],expected_pages,"total_pages")

    # Resource schema validation
    resource_ids = set()
    for resource in body["data"]:
        assert_key_present(resource,["id", "name", "year", "color", "pantone_value"])

        assert isinstance(resource["id"], int)
        assert isinstance(resource["name"], str)

        assert resource["id"] not in resource_ids
        resource_ids.add(resource["id"])


@pytest.mark.smoke
def test_get_single_resource(api_client,test_data):
    data=test_data["resource_id"]
    id=data["valid_id"]["id"]
    email=data["expected_data"]["name"]
    response = api_client.get(f"/unknown/{id}")
    body=response.json()

    assert_key_present(body["data"],["id", "name", "year", "color", "pantone_value"])

    assert_value(response.status_code,data["expected_data"]["success"],"status_code")
    assert_value(body["data"]["id"],id,"id")
    assert_value(body["data"]["name"],email,"name")

@pytest.mark.regression
def test_get_invalid_user(api_client,test_data):
    data=test_data["resource_id"]
    id=data["invalid_id"]["id"]
    response = api_client.get(f"/unknown/{id}")
    body=response.json()
    assert_value(body,data["expected_data"]["no_data"],"body")
    assert_value(response.status_code,data["expected_data"]["bad_request"],"status_code")

