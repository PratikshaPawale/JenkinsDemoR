import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """Launches a reusable Playwright browser instance for browser-based tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def api_request_context():
    """Creates a Playwright APIRequestContext configured for Typicode."""
    p = sync_playwright().start()
    request = p.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    yield request
    request.dispose()
    p.stop()
