import pytest
from playwright.sync_api import APIRequestContext

@pytest.mark.api
@pytest.mark.xfail(reason="Бэкенд возвращает 404 Not Found согласно баг-репорту bug-11")
def test_api_generate_sharing_uuid(api_request_context: APIRequestContext):
    """Поток 4: Проверка генерации UUID-токена для шеринга сборки"""
    payload = {
        "location": "Горнолыжный курорт",
        "dates": ["2026-12-01", "2026-12-10"],
        "guests": {"adults": 2, "children": 0}
    }
    
    response = api_request_context.post("/api/v1/sharing/generate", data=payload)
    assert response.ok
