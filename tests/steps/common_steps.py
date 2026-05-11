from pytest_bdd import given, when, then, parsers
from utils.logger import get_logger

logger=get_logger(__name__)

@given("the API client is available")
def api_available(api_client,request):
    test_name = request.node.name
    logger.info(f"[{test_name}] Getting API Client")
    return api_client


@when(parsers.parse('I send "{HTTP_TYPE}" request to "{endpoint}" for "{user_action}"'),target_fixture="response")
def request_users(api_client,HTTP_TYPE,endpoint,test_data,user_action,request):
    logger.info(
        f"TEST: {request.node.name} | "
        f'BDD step for request users:"{HTTP_TYPE}" request to "{endpoint}" for "{user_action}" '
    )
    data=test_data[user_action]
    params = {
    "valid_id": data["valid_payload"]["id"],
    "invalid_id": data["invalid_payload"]["id"]
    }
    logger.debug(f"Path params: {params}")

    endpoint = endpoint.format(**params)
    request.node._endpoint = endpoint
    http_method=getattr(api_client,HTTP_TYPE.lower())
    logger.debug(f"http_mthod:{http_method}")
    return http_method(endpoint)