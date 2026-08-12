import pytest
from utils.api_helpers import APIHelpers
from utils.data_loader import load_json
from utils.assertions import assert_status_code, assert_json_contains, assert_key_present


@pytest.mark.api
def test_TC010_get_post_by_id(api_request_context):
    """TC010 - Verify GET /posts/1 returns expected data"""
    expected = load_json("expected_data.json")["post_1"]
    api = APIHelpers(api_request_context)
    resp = api.get("/posts/1")
    assert_status_code(resp, 200)
    json_data = resp.json()
    assert_json_contains(json_data, expected)


@pytest.mark.api
def test_TC011_create_post(api_request_context):
    """TC011 - Verify POST /posts creates a post and returns 201/201-like response"""
    post_payload = load_json("post_data.json")
    api = APIHelpers(api_request_context)
    resp = api.post("/posts", json=post_payload)
    # Typicode returns 201 for created resources
    assert_status_code(resp, 201)
    json_data = resp.json()
    assert_key_present(json_data, "id")
    # The API echoes back title/body/userId
    for k in ("title", "body", "userId"):
        assert json_data.get(k) == post_payload.get(k)
