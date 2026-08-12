import pytest
from utils.api_helpers import APIHelpers
from utils.data_loader import load_json
from utils.assertions import assert_status_code


@pytest.mark.api
def test_TC001_get_root(api_request_context):
    """TC001 - Verify base endpoint is reachable"""
    api = APIHelpers(api_request_context)
    resp = api.get("/")
    assert_status_code(resp, 200)


@pytest.mark.api
def test_TC002_get_posts_list(api_request_context):
    """TC002 - Verify posts list endpoint returns 200"""
    api = APIHelpers(api_request_context)
    resp = api.get("/posts")
    assert_status_code(resp, 200)
    data = resp.json()
    assert isinstance(data, list)
