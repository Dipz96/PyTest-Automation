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