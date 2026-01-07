import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
import os
from datetime import datetime


@pytest.fixture(scope="session")
def browser():
    """Create browser instance for the session"""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture
def context(browser):
    """Create a new browser context for each test"""
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True
    )
    yield context
    context.close()


@pytest.fixture
def page(context):
    """Create a new page for each test"""
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def base_url():
    """Base URL for the application"""
    return "https://www.saucedemo.com/"


def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as regression test"
    )
    config.addinivalue_line(
        "markers", "login: mark test as login test"
    )
    config.addinivalue_line(
        "markers", "product: mark test as product test"
    )
    config.addinivalue_line(
        "markers", "cart: mark test as cart test"
    )
    config.addinivalue_line(
        "markers", "checkout: mark test as checkout test"
    )
