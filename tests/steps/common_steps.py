from pytest_bdd import given, when, then, parsers
@given("the API client is available")
def api_available(api_client):
    return api_client


@when(parsers.parse('I send "{HTTP_TYPE}" request to "{endpoint}" for "{user_action}"'),target_fixture="response")
def request_users(api_client,HTTP_TYPE,endpoint,test_data,user_action,request):
    data=test_data[user_action]
    params = {
    "valid_id": data["valid_payload"]["id"],
    "invalid_id": data["invalid_payload"]["id"]
    }
    print("params:{params}")

    endpoint = endpoint.format(**params)
    request.node._endpoint = endpoint
    http_method=getattr(api_client,HTTP_TYPE.lower())
    print(f"http_mthod:{http_method}")
    return http_method(endpoint)