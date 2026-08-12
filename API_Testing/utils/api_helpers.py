from typing import Any, Dict
import json as _json
from playwright.sync_api import APIRequestContext


class APIHelpers:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def get(self, path: str, params: Dict[str, Any] = None):
        return self.request.get(path, params=params)

    def post(self, path: str, json: Dict[str, Any] = None, payload: Dict[str, Any] = None):
        body_payload = json if json is not None else payload
        body = _json.dumps(body_payload or {})
        return self.request.post(path, data=body, headers={"Content-Type": "application/json"})

    def put(self, path: str, json: Dict[str, Any] = None, payload: Dict[str, Any] = None):
        body_payload = json if json is not None else payload
        body = _json.dumps(body_payload or {})
        return self.request.put(path, data=body, headers={"Content-Type": "application/json"})

    def delete(self, path: str):
        return self.request.delete(path)
