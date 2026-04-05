from datetime import datetime, timezone

def assert_key_present(body,keys):
    if isinstance(keys,str):
        assert keys in body, f"Expected key '{keys}' not found in response"
    elif isinstance(keys,list):
        for key in keys:
            assert key in body, f"Expected key '{key}' not found in response"
    else:
        raise TypeError("keys must be a string or list of strings")
    

def assert_value(actual,expected,field_name):
    assert actual == expected, (
        f"Expected {field_name} to be '{expected}', but got '{actual}'"
    )
    print(f"Assertion PASSED: {field_name} - Value '{actual}' matches expected '{expected}'")


def assert_updationTime(updationTime):
    expected_dttime = datetime.now(timezone.utc)
    actual_dttime = datetime.fromisoformat(updationTime.replace("Z", "+00:00"))
    assert abs((expected_dttime - actual_dttime).total_seconds()) < 60, (
        f"Updation time is not within expected limit of 60 s"
    )
    print(f"Assertion PASSED: UpdationTime - Value '{actual_dttime}' matches expected '{expected_dttime}'")


def assert_response_time(response,timeduration):
    assert response.elapsed.total_seconds() >= timeduration, (
        f"Expected response time > {timeduration}s, got {response.elapsed.total_seconds()}s"
    )
    print(f"Assertion PASSED: Expected response time > {timeduration}s")