import pytest
import pytest_html
from playwright.sync_api import sync_playwright, APIRequestContext, Page

@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://elmobil.ru"

@pytest.fixture(scope="session")
def api_request_context(base_url: str) -> APIRequestContext:
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url=base_url,
            extra_http_headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )
        yield request_context
        request_context.dispose()

# Автоматическое добавление скриншота экрана в HTML-отчет при падении любого UI теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    
    if report.when == "call" and report.failed:
        if "page" in item.funcargs:
            page: Page = item.funcargs["page"]
            screenshot_base64 = page.screenshot(type="png", full_page=False).hex()
            extra.append(pytest_html.extras.image(screenshot_base64, mime_type="image/png"))
            report.extra = extra
