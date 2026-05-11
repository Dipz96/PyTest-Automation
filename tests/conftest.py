import pytest
import json
from api.client import APIClient
from utils.logger import get_logger

logger = get_logger(__name__)

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



@pytest.fixture(scope="module")
def test_data(pytestconfig):
    root = pytestconfig.rootpath
    file_path = root / "test_data" / "test_data.json"

    if not file_path.exists():
        pytest.fail(f"Test data file not found at {file_path}")

    with open(file_path) as f:
        return json.load(f)
    
@pytest.fixture
#context fixture for communicating / storing values for immediate steps in a dict form->Aletrnative  to target_fixture
def context():
    return {}
    
@pytest.fixture(scope="module", autouse=True)
def log_test_file_lifecycle(request):
    module_name = request.module.__name__
    logger.info(f"========== START TEST: {module_name} ==========")
    yield
    logger.info(f"========== END TEST: {module_name} ==========")