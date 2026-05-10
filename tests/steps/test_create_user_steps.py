import pytest
import json
from pytest_bdd import scenarios
from pytest_bdd import given, when, then, parsers
from utils.assertions import assert_value,assert_key_present,assert_response_time
from utils.validators import VALIDATION_MAP
from utils.helpers import get_execution_time
from tests.steps.common_steps import *
import re


pytestmark = pytest.mark.api #mark all api tests

scenarios("../features/create_user.feature")


@given(parsers.parse('I have payload with name "{name}" and job "{job}"'))
def set_payload(context, name, job):
    context["payload"] = {
        "name": name,
        "job": job
    }

@when(parsers.parse('I send POST request to "{endpoint}"'))
def create_user(api_client,context, endpoint):
    payload=context.get("payload",{})

    response=api_client.post(endpoint,json=payload)

    context["response"]=response
    context["body"]=response.json()

@then(parsers.parse("the response status should be {status:d}"))
def check_status(context,status):
    response=context["response"]
    assert_value(response.status_code,status,"status_code")

@then('the response should contain created user details')
def validate_response(context):
    body = context["body"]
    payload = context["payload"]

    assert "id" in body
    assert "createdAt" in body

    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
