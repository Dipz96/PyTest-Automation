import pytest
import math
import logging
from pytest_bdd import scenarios
from pytest_bdd import given, when, then, parsers
from utils.assertions import assert_value,assert_key_present,assert_response_time
from utils.validators import VALIDATION_MAP
from utils.helpers import get_execution_time

pytestmark = pytest.mark.api #mark all api tests

#Tests can also be marked here, instead of feature file
# @pytest.mark.regression
# @scenario("../features/users.feature", "Get list of users")
# def test_get_users():
#     pass

scenarios("../features/get_users.feature")

@given("the API client is available")
def api_available(api_client):
    return api_client

@when(parsers.parse('I send GET request to "{endpoint}"'),target_fixture="response")
def request_users(api_client,endpoint,test_data,request):
    data=test_data["user_id"]
    params = {
    "valid_id": data["valid_id"]["id"],
    "invalid_id": data["invalid_id"]["id"]
    }

    endpoint = endpoint.format(**params)
    request.node._endpoint = endpoint
    return api_client.get(endpoint)

@then(parsers.parse("the response status should be {status:d}"))
def check_status(response,status):
    assert_value(response.status_code,status,"status_code")

@then(parsers.parse('the response should match test data "{key}"'))
def validate_response(response, test_data , key,request):
    body = response.json()

    if key not in VALIDATION_MAP:
        raise ValueError(f"No validator found for key: {key}")

    VALIDATION_MAP[key](body, test_data=test_data,request=request)


@then(parsers.parse('the response time should match test data "{delay}"'))
def validate_response_time(response, delay,request):
    endpoint=request.node._endpoint
    assert_response_time(response, get_execution_time(endpoint))




