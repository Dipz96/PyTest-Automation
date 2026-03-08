import pytest
import json
from api.client import APIClient

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"

@pytest.fixture(scope="session")
def headers():
    return {
        "x-api-key": "reqres_ffb7036fe607421eb2f12f43b9897496",
        "Content-Type": "application/json"
    }

@pytest.fixture(scope='session')
def api_client(base_url,headers):
    return APIClient(base_url,headers)

import json
from pathlib import Path
import pytest

@pytest.fixture(scope="module")
def test_data(pytestconfig):
    root = pytestconfig.rootpath
    file_path = root / "test_data" / "test_data.json"

    if not file_path.exists():
        pytest.fail(f"Test data file not found at {file_path}")

    with open(file_path) as f:
        return json.load(f)
    
@pytest.fixture(scope="module", autouse=True)
def log_test_file_lifecycle(request):
    module_name = request.module.__name__
    print(f"\n===== Starting test file: {module_name} =====")
    yield
    print(f"\n===== Finished test file: {module_name} =====")