import pytest
from utils.api_helpers import APIHelpers
from utils.assertions import assert_status_code


@pytest.mark.api
def test_TC020_get_users_list(api_request_context):
    """TC020 - Verify GET /users returns a list of users"""
    api = APIHelpers(api_request_context)
    resp = api.get("/users")
    assert_status_code(resp, 200)
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.api
def test_TC021_get_user_by_id(api_request_context):
    """TC021 - Verify GET /users/1 contains expected fields"""
    api = APIHelpers(api_request_context)
    resp = api.get("/users/1")
    assert_status_code(resp, 200)
    json_data = resp.json()
    assert "id" in json_data and json_data["id"] == 1
    assert "email" in json_data
