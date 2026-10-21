import pytest
import pytest_html
from playwright.sync_api import Page

@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://elmobil.ru"

# Автоматическое добавление скриншота в HTML-отчет при падении UI-теста
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
