from typing import Any, Dict


def assert_status_code(response, expected_code: int):
    actual = response.status
    assert actual == expected_code, f"Expected status {expected_code}, got {actual}"


def assert_json_contains(response_json: Dict[str, Any], expected: Dict[str, Any]):
    for k, v in expected.items():
        assert k in response_json, f"Key '{k}' not found in response"
        assert response_json[k] == v, f"For key '{k}', expected '{v}', got '{response_json[k]}'"


def assert_key_present(response_json: Dict[str, Any], key: str):
    assert key in response_json, f"Expected key '{key}' in response"
