import pytest
from pytest_bdd import scenarios
from pytest_bdd import given, when, then, parsers
from utils.assertions import assert_value,assert_key_present,assert_response_time
from utils.validators import VALIDATION_MAP
from utils.helpers import get_execution_time
from tests.steps.common_steps import *
from utils.logger import get_logger


pytestmark = pytest.mark.api #mark all api tests
logger=get_logger(__name__)

#Tests can also be marked here, instead of feature file
# @pytest.mark.regression
# @scenario("../features/users.feature", "Get list of users")
# def test_get_users():
#     pass

scenarios("../features/get_users.feature")

@then(parsers.parse("the response status should be {status:d}"))
def check_status(response,status):
    logger.debug(f"BDD Step started: response expected status is {status}")
    assert_value(response.status_code,status,"status_code")

@then(parsers.parse('the response should match test data "{key}"'))
def validate_response(response, test_data , key,request):
    logger.debug(f"BDD Step started:")
    body = response.json()

    if key not in VALIDATION_MAP:
        logger.error(f"Key:{key} - not in VALIDATION_MAP:{VALIDATION_MAP}")
        raise ValueError(f"No validator found for key: {key}")

    VALIDATION_MAP[key](body, test_data=test_data,request=request)


@then(parsers.parse('the response time should match test data "{delay}"'))
def validate_response_time(response, delay,request):
    endpoint=request.node._endpoint
    assert_response_time(response, get_execution_time(endpoint))




