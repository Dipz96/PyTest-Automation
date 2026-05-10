import pytest
import math
import logging
from pytest_bdd import scenarios
from pytest_bdd import given, when, then, parsers
from utils.assertions import assert_value,assert_key_present,assert_response_time
from utils.validators import VALIDATION_MAP
from utils.helpers import get_execution_time
from tests.steps.common_steps import *

pytestmark = pytest.mark.api #mark all api tests

scenarios("../features/delete_users.feature")

@when(parsers.parse('I send POST request to "{endpoint}" for delete_user'),target_fixture="response")
def request_users(api_client,endpoint,test_data,request):
    data=test_data["delete_user"]
    params = {
    "valid_id": data["valid_payload"]["id"],
    }
    endpoint = endpoint.format(**params)
    request.node._endpoint = endpoint
    return api_client.delete(endpoint)

@then(parsers.parse("the response status should be {status:d}"))
def check_status(response,status):
    assert_value(response.status_code,status,"status_code")